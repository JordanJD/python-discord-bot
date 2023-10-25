"""Module manages Cog for GPT test"""
import requests
from discord.ext import commands
from dotenv import dotenv_values

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": dotenv_values(".env").get('RAPID_API_KEY'),
    "X-RapidAPI-Host": dotenv_values(".env").get('RAPID_API_HOST')
}

class GptCog(commands.Cog):
    """Initialize GPT Cog"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gpt(self, ctx):
        """runs a test hitting chatgpt integration and returns response to bot """
        endpoint =  'https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions'
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": "Hello, how are you?"
                }
            ]
        }
        try:
            response = requests.post(endpoint,json=payload,headers=headers,timeout=5000)
            print(response.content)
            await ctx.send(response.json())
        except requests.exceptions.RequestException as e:
            print(e)
            await ctx.send(e)