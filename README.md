![version](https://img.shields.io/badge/version-0.6.0-orange)
![python](https://img.shields.io/badge/python-3.6|3.7-blue)

# Discord Bot CLI

An easy way to keep your discord bot projects consistant and work with their database using the command line. Inspired by [Orator ORM](https://github.com/sdispater/orator).

## Installation 

pip install discord-bot-cli

## Overview
Prefix: `dbot`

Available commands:
```
branches          Available branches of the discord bot
docstring         Generate a docstring based on a table name
help              Displays help for a command
list              Lists commands
migrate           Run the database migrations.
new               Creates a new discord bot base.
db
db:seed           Seed the database with records.
make
make:cog          Creates a new Cog extension.
make:command      Creates a new Command extension.
make:migration    Create a new migration file.
make:model        Creates a new Model class.
make:seed         Create a new seeder file.
migrate
migrate:install   Create the migration repository.
migrate:refresh   Reset and re-run all migrations.
migrate:reset     Rollback all database migrations.
migrate:rollback  Rollback the last database migration.
migrate:status    Show a list of migrations up/down.
```

### Usage
This package is built off of the Orator ORM and most of the commands work the same way as in their [documentation](https://orator-orm.com/docs/0.9/). 

You can create a new bot directory `bot_project` and pre-load your token like this:
```cmd
dbot new bot_project --token=8675309 
```
You can always change the token and your database connections in the `config.yaml` file in your projects main directory.

CD into the project directory and you can easily add a cog/command using the `make` command:
```cmd
dbot make:cog new_cog
dbot make:command new_command
```

### Requirements

```
orator==0.9.9
requests
```


## License

This project is licensed under MIT - see the [LICENSE](LICENSE) file for details.

### Notes

Here is the bot scaffolding the cli will download. Different versions can be specified with the `-b, --branch=BRANCH` option for the new command.

Documentation for the [Orator ORM](https://orator-orm.com/docs/0.9/)

Documentation for [discord.py](https://discordpy.readthedocs.io/en/latest/)
