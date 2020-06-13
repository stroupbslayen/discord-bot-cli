# -*- coding: utf-8 -*-

from pathlib import Path

import inflection
from cleo import Command

from ...templates import model


class ModelMakeCommand(Command):
    """
    Creates a new Model class.

    make:model
        {name : The name of the model to create.}
        {--m|migration : Create a new migration file for the model.}
        {--p|path= : Path to models directory}
    """

    def handle(self):
        name = self.argument("name")
        self.cwd = Path().cwd()
        singular = inflection.singularize(inflection.tableize(name))
        filepath = self._get_path(f"{singular}.py")

        if filepath.is_file():
            raise RuntimeError("The model file already exists.")

        parent = self.cwd.joinpath("__init__.py")
        if not parent.is_file():
            parent.touch()

        stub = self._get_stub()
        stub = self._populate_stub(name, stub)

        with open(filepath, "w") as f:
            f.write(stub)

        self.info(f"Model <comment>{name}</> successfully created.")

        if self.option("migration"):
            table = inflection.tableize(name)

            self.call(
                "make:migration",
                [
                    ("name", "create_%s_table" % table),
                    ("--table", table),
                    ("--create", True),
                ],
            )

    def _get_stub(self):
        """
        Get the model stub template

        :rtype: str
        """
        return model

    def _populate_stub(self, name, stub):
        """
        Populate the placeholders in the migration stub.

        :param name: The name of the model
        :type name: str

        :param stub: The stub
        :type stub: str

        :rtype: str
        """
        return stub.format(
            name=inflection.camelize(name),
            name_plural=inflection.pluralize(name).lower(),
        )

    def _get_path(self, name=None):
        if self.option("path"):
            directory = Path(self.option("path"))
        else:
            directory = Path().cwd().joinpath("bot", "database", "models")
        if name:
            return directory.joinpath(name)

        return directory
