from setuptools import setup

import discord_bot_cli

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="discord-bot-cli",
    version=discord_bot_cli.__version__,
    description="A discord bot project helper with a useful command line interface",
    packages=["discord_bot_cli", "discord_bot_cli.commands"],
    url="https://github.com/stroupbslayen/discord-bot-cli",
    author="StroupBSlayen",
    author_email="",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6.0",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    install_requires=["discord.py>=1.2.4", "orator==0.9.9", "requests"],
    keywords=["discord", "discord.py", "orator", "discord bot"],
    include_package_data=True,
    py_modules=["discord_bot_cli"],
    entry_points={
        "console_scripts": [
            "dbot = discord_bot_cli.commands.application:application.run"
        ]
    },
)
