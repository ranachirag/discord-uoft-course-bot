import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path='.env')
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready')

client.run(TOKEN)
