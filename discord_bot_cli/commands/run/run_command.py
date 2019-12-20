import importlib.util as util
from pathlib import Path

from cleo import Command


class RunCommand(Command):
    """
    Run your discord bot.

    run
    """

    def handle(self):
        cwd = Path().cwd()
        pkg = cwd.joinpath("bot")
        init = pkg.joinpath("__init__.py")
        pkg = self._load_file(str(pkg), str(init))

        # bot.run()

    def _load_file(self, name, cwd):
        spec = util.spec_from_file_location(name, cwd)
        package = util.module_from_spec(spec)
        spec.loader.exec_module(package)
        return package
