""" Module to control discord bot and commands"""
import discord
from discord.ext import commands
from dotenv import dotenv_values
from cogs.help import HelpCog
from cogs.workout import WorkoutCog
from cogs.gpt import GptCog

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    """function that runs on successful bot start"""
    await bot.add_cog(HelpCog(bot))
    await bot.add_cog(WorkoutCog(bot))
    await bot.add_cog(GptCog(bot))
    print("online")

@bot.command(name="ping")
async def ping(context):
    """Test command to check if bot is working"""
    await context.send("pong")

bot.run(dotenv_values(".env").get('DISCORD_TOKEN')) # type: ignore
