# -*- coding: utf-8 -*-

import os

import inflection
from cleo import Command
from orator.utils import mkdir_p

from ...templates import cog


class CogMakeCommand(Command):
    """
    Creates a new Cog extension.

    make:cog
        {name : The name of the cog to create.}
    """

    def handle(self):
        name = self.argument("name")

        singular = inflection.singularize(inflection.tableize(name))
        directory = self._get_path()
        filepath = self._get_path(singular + ".py")

        if os.path.exists(filepath):
            raise RuntimeError("The cog extension already exists.")

        mkdir_p(directory)
        stub = self._get_stub()
        stub = self._populate_stub(name, stub)
        with open(filepath, "w") as f:
            f.write(stub)

        self.info(f"Cog <comment>'{name}'</> successfully created.")

    def _get_stub(self):
        """
        Get the cog stub template

        :rtype: str
        """
        return cog

    def _populate_stub(self, name, stub):
        """
        Populate the placeholders in the migration stub.

        :param name: The name of the model
        :type name: str

        :param stub: The stub
        :type stub: str

        :rtype: str
        """
        return stub.format(name=inflection.camelize(name))

    def _get_path(self, name=None):

        directory = os.path.join(os.getcwd(), "bot/extensions/cogs")

        if name:
            return os.path.join(directory, name)

        return directory
