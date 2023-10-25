"""Module manages Cog for workout parsing"""
from discord.ext import commands

class WorkoutCog(commands.Cog):
    """Initialize Workout Cog"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def workout(self, ctx, arg):
        """command that will be used to parse workouts using chatgpt integration"""
        await ctx.send(arg)
