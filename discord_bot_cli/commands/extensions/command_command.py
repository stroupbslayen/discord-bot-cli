# -*- coding: utf-8 -*-

import os

import inflection
from cleo import Command
from orator.utils import mkdir_p

from ...templates import command


class CommandMakeCommand(Command):
    """
    Creates a new Command extension.

    make:command
        {name : The name of the cog to create.}
    """

    def handle(self):
        name = self.argument("name").lower()
        directory = self._get_path()
        filepath = self._get_path(name + ".py")

        if os.path.exists(filepath):
            raise RuntimeError("The command extension already exists.")

        mkdir_p(directory)

        stub = self._get_stub()
        stub = self._populate_stub(name, stub)

        with open(filepath, "w") as f:
            f.write(stub)

        self.info(f"Command <comment>'{name}'</> successfully created.")

    def _get_stub(self):
        """
        Get the model stub template

        :rtype: str
        """
        return command

    def _populate_stub(self, name, stub):
        """
        Populate the placeholders in the migration stub.

        :param name: The name of the model
        :type name: str

        :param stub: The stub
        :type stub: str

        :rtype: str
        """
        return stub.format(name=name.lower())

    def _get_path(self, name=None):

        directory = os.path.join(os.getcwd(), "bot/extensions/commands")

        if name:
            return os.path.join(directory, name)

        return directory
