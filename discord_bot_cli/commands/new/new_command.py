# -*- coding: utf-8 -*-
from pathlib import Path

import inflection
import yaml
from cleo import Command

from .git_handler import GitHandler
from ...templates.simple import simple


class NewCommand(Command):
    """
    Creates a new discord bot base.

    new
        {name : The name of the project to create.}
        {--b|branch= : Specifiy a branch of discord_bot repo to use}
        {--t|token= : Pre load the discord bot token into the config}
        {--s|simple : Creates a simple single file bot}
    """

    def handle(self):
        branch = None
        name = self.argument("name")
        singular = inflection.singularize(inflection.tableize(name))
        cwd = Path()
        TOKEN = self.option("token")
        if self.option("simple"):
            cwd.joinpath(f"{name}.py").write_text(simple(TOKEN))
            if TOKEN:
                self.info("Token has been added")
            return self.info(
                f"Simple bot: {name}.py has been successfully created\nYou'll need to install discord.py if it's not already installed!"
            )
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
                path = cwd.joinpath(name, "config.yaml")
                with open(path, "r") as file:
                    text = file.read()

                with open(path, "w") as file:
                    file.write(text.replace("TOKEN:\n", f"TOKEN: {TOKEN}"))

                self.info("Token has been successfully added.")
            self.info("You can now CD into the directory to install the requirements")
        else:
            self.warning(f"Ran into an error retrieveing branch {version}")
