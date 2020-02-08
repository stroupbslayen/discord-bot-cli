from pathlib import Path

import yaml
from cleo import Command
from orator import DatabaseManager


class MakeDocstringCommand(Command):
    """
    Generate a docstring based on a table name
    docstring
        {table : Name of the table to generate the docstring for}
        {--c|connection=default : The connection to use}
    """

    @staticmethod
    def columns(connection):
        info = ""
        for name, column in connection.items():
            length = "({})".format(column._length) if column._length else ""
            info += "{}: {}{} default: {}\n\n".format(
                name, column.get_type(), length, column.get_default()
            )
        return info

    def handle(self):

        file = Path("config.yaml")
        if not file.is_file():
            return self.warning("Unable to find a valid config file!")

        config = yaml.load(file.read_text(), Loader=yaml.FullLoader)

        DB = DatabaseManager(config=config.get("databases"))

        if self.option("connection") == "default":
            conn = DB.get_schema_manager().list_table_columns(self.argument("table"))
        else:
            conn = (
                DB.connection(self.option("connection"))
                .get_schema_manager()
                .list_table_columns(self.argument("table"))
            )

        docstring = f'"""Model Docstring\n\n{self.columns(conn)}\n"""'

        print(docstring)
