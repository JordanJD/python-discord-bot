"""Module manages Cog for help command"""
import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    """Initialize Help Cog"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        """The current available bot commands"""
        embed = discord.Embed(title="Available commands", description="Choose from the following commands")
        embed.add_field(name="Show this help", value = "`/help`", inline = False)
        embed.add_field(name="Test to see if I am working", value="`/ping`", inline=False)
        embed.add_field(name="Log a workout", value="`/workout`", inline=False)
        await ctx.send(embed=embed)
