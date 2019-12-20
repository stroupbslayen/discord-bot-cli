# -*- coding: utf-8 -*-
from pathlib import Path

import inflection
import yaml
from cleo import Command

from .git_handler import GitHandler


class NewCommand(Command):
    """
    Creates a new discord bot base.

    new
        {name : The name of the project to create.}
        {--b|branch= : Specifiy a branch of discord_bot repo to use}
        {--t|token= : Pre load the discord bot token into the config}
    """

    def handle(self):
        branch = None
        name = self.argument("name")
        singular = inflection.singularize(inflection.tableize(name))
        cwd = Path()
        handler = GitHandler(cwd)
        version = self.option("branch")
        if version:
            branch = handler.get_branch(version)
            if not branch:
                self.warning(f"Unable to retrieve branch {version}")
                return
        else:
            branch = handler.get_latest_branch()
        if branch:
            self.info(f"Using branch {branch.name}")
            handler.unzip(name, branch)

            self.info(f"Bot <comment>'{name}'</> successfully created.")

            if self.option("token"):
                TOKEN = self.option("token")
                path = cwd.joinpath(name, "config.yaml")
                with open(path, "r") as file:
                    text = file.read()

                with open(path, "w") as file:
                    file.write(text.replace("TOKEN:\n", f"TOKEN: {TOKEN}"))

                self.info(f"Token has been successfully added.")

        else:
            self.warning(f"Ran into an error retrieveing branch {version}")
