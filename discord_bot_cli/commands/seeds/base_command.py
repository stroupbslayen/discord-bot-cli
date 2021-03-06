# -*- coding: utf-8 -*-

import os

from ..command import Command


class BaseCommand(Command):
    def _get_seeders_path(self):
        return os.path.join(os.getcwd(), "bot/database/seeds")
