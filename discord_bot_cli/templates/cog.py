cog = """
import discord
from discord.ext import commands


class {name}(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Cog '{name}' is ready")

    @commands.command()
    async def {name}Ping(self,ctx:commands.Context):
        await ctx.send("pong")

def setup(bot):
    bot.add_cog({name}(bot))


"""
