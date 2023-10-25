""" Module to control discord bot and commands"""
import discord
import requests
from discord.ext import commands
from dotenv import dotenv_values

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

CHAT_GPT_BASE_URL = 'https://chatgpt-best-price.p.rapidapi.com/v1'
COMPLETIONS_URL = 'https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions'
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": dotenv_values(".env").get('RAPID_API_KEY'),
    "X-RapidAPI-Host": dotenv_values(".env").get('RAPID_API_HOST')
}
@bot.event
async def on_ready():
    """function that runs on successful bot start"""
    print("online")

@bot.command(name='workout')
async def workout(context):
    """Main bot command that will be used to parse workouts"""
    await context.send()

@bot.command(name="ping")
async def ping(context):
    """Test command to check if bot is working"""
    await context.send("pong")

@bot.command(name='gpt')
async def gpt(context):
    """runs a test hitting chatgpt integration and returns response to bot """
    endpoint =  CHAT_GPT_BASE_URL + '/chat/completions'
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": "Hello, how are you?"
            }
        ]
    }
    response = requests.post(endpoint,json=payload,headers=headers,timeout=5000)
    print(response.content)
    await context.send(response.json())

bot.run(dotenv_values(".env").get('DISCORD_TOKEN')) # type: ignore
