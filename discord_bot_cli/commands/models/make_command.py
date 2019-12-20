# -*- coding: utf-8 -*-

import os

import inflection
from cleo import Command
from orator.utils import mkdir_p

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

        singular = inflection.singularize(inflection.tableize(name))
        directory = self._get_path()
        filepath = self._get_path(singular + ".py")

        if os.path.exists(filepath):
            raise RuntimeError("The model file already exists.")

        mkdir_p(directory)

        parent = os.path.join(directory, "__init__.py")
        if not os.path.exists(parent):
            with open(parent, "w"):
                pass

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
        stub = stub.format(name=inflection.camelize(name))

        return stub

    def _get_path(self, name=None):
        if self.option("path"):
            directory = self.option("path")
        else:
            directory = os.path.join(os.getcwd(), "bot/database/models")

        if name:
            return os.path.join(directory, name)

        return directory
