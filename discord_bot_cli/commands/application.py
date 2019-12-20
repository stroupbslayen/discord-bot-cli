# -*- coding: utf-8 -*-

from cleo import Application

from .. import __application__, __version__
from .extensions import CogMakeCommand, CommandMakeCommand

# Migrations
from .migrations import (
    InstallCommand,
    MigrateCommand,
    MigrateMakeCommand,
    RefreshCommand,
    ResetCommand,
    RollbackCommand,
    StatusCommand,
)

# Models
from .models import ModelMakeCommand

# New Project
from .new import NewCommand, VersionCommand
from .run import RunCommand

# Seeds
from .seeds import SeedCommand, SeedersMakeCommand

application = Application(__application__, __version__, complete=True)


application.add(InstallCommand())
application.add(MigrateCommand())
application.add(MigrateMakeCommand())
application.add(RollbackCommand())
application.add(StatusCommand())
application.add(ResetCommand())
application.add(RefreshCommand())


application.add(SeedersMakeCommand())
application.add(SeedCommand())


application.add(ModelMakeCommand())


application.add(NewCommand())
application.add(VersionCommand())

# Extensions


application.add(CogMakeCommand())
application.add(CommandMakeCommand())

# Run

# Maybe eventually I'll get this to work...
# application.add(RunCommand())
