command = """
import discord
from discord.ext import commands


@commands.command()
async def {name}(self):
    print(f"loaded command: {name}")


def setup(bot):
    bot.add_command({name})

"""

