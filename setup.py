from setuptools import setup

import discord_bot_cli

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name=discord_bot_cli.__application__,
    version=discord_bot_cli.__version__,
    description=discord_bot_cli.__description__,
    packages=["discord_bot_cli", "discord_bot_cli.commands"],
    url=discord_bot_cli.__url__,
    author=discord_bot_cli.__author__,
    author_email="",
    license=discord_bot_cli.__license__,
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
