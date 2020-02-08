top = """import discord
from discord.ext import commands"""

middle = '\n\nTOKEN = "{token}"\n\n'
bottom = """bot = commands.Bot(command_prefix="!")
invite_link = "https://discordapp.com/api/oauth2/authorize?client_id={}&scope=bot"


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")
    print(f"With ID: {bot.user.id}")
    print(invite_link.format(bot.user.id))


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


bot.run(TOKEN)"""


def simple(token):
    return f"""{top}{middle.format(token=token)}{bottom}"""

