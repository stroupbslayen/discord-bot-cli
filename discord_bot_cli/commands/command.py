# -*- coding: utf-8 -*-

import os

import yaml
from cleo import Command as BaseCommand
from cleo import InputOption, ListInput
from orator import DatabaseManager


class Command(BaseCommand):

    needs_config = True

    def __init__(self, resolver=None):
        self.resolver = resolver
        self.input = None
        self.output = None

        super(Command, self).__init__()

    def configure(self):
        super(Command, self).configure()

        if self.needs_config and not self.resolver:
            # Checking if a default config file is present
            if not self._check_config():
                self.add_option(
                    "config", "c", InputOption.VALUE_REQUIRED, "The config file path"
                )

    def execute(self, i, o):
        """
        Executes the command.
        """
        self.set_style("question", fg="blue")

        if self.needs_config and not self.resolver:
            self._handle_config(self.option("config"))

        return self.handle()

    def call(self, name, options=None):
        command = self.get_application().find(name)
        command.resolver = self.resolver

        return super(Command, self).call(name, options)

    def call_silent(self, name, options=None):
        command = self.get_application().find(name)
        command.resolver = self.resolver

        return super(Command, self).call_silent(name, options)

    def confirm_to_proceed(self, message=None):
        if message is None:
            message = "Do you really wish to run this command?: "

        if self.option("force"):
            return True

        confirmed = self.confirm(message)

        if not confirmed:
            self.comment("Command Cancelled!")

            return False

        return True

    def _get_migration_path(self):
        return os.path.join(os.getcwd(), "bot/database/migrations")

    def _check_config(self):
        """
        Check presence of default config files.

        :rtype: bool
        """
        current_path = os.path.relpath(os.getcwd())

        accepted_files = ["config.yaml", "config.yml", "config.py"]
        for accepted_file in accepted_files:
            config_file = os.path.join(current_path, accepted_file)
            if os.path.exists(config_file) and self._handle_config(config_file):
                return True

        return False

    def _handle_config(self, config_file):
        """
        Check and handle a config file.

        :param config_file: The path to the config file
        :type config_file: str

        :rtype: bool
        """
        config = self._get_config(config_file)

        self.resolver = DatabaseManager(
            config.get("databases", config.get("DATABASES", {}))
        )

        return True

    def _get_config(self, path=None):
        """
        Get the config.

        :rtype: dict
        """
        if not (path or self.option("config")):
            raise Exception("The --config|-c option is missing.")

        if not path:
            path = self.option("config")

        filename, ext = os.path.splitext(path)
        if ext in [".yml", ".yaml"]:
            with open(path) as fd:
                config = yaml.load(fd, Loader=yaml.FullLoader)

        elif ext in [".py"]:
            config = {}

            with open(path) as fh:
                exec(fh.read(), {}, config)
        else:
            raise RuntimeError("Config file [%s] is not supported." % path)
        return CleanConfig(config).cleaned


class CleanConfig:
    def __init__(self, config):
        self.default_config = config

    def _clean(self, name, settings):
        if name.lower() != "default":
            to_delete = [key for key, value in settings.items() if not value]
            for item in to_delete:
                del settings[item]
        return {name: settings}

    @property
    def cleaned(self):
        clean_config = self.default_config
        for name, settings in tuple(clean_config["databases"].items()):
            clean_config["databases"].update(self._clean(name, settings))
        return clean_config
