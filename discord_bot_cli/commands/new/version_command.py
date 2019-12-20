# -*- coding: utf-8 -*-
from pathlib import Path

from cleo import Command

from .git_handler import GitHandler


class VersionCommand(Command):
    """
    Available branches of the discord bot

    branches
        
    """

    def handle(self):
        cwd = Path()
        handler = GitHandler(cwd)
        try:
            for branch in handler._get_branches():
                self.info(f"v{branch.name}")
        except:
            self.warning("Unable to retrieve branches")
