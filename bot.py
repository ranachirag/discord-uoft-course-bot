import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path='.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.command(name='find', help='Gives an overview of the course requested')
async def ind(ctx, course):
    response = course
    await ctx.send(response)

client.run(TOKEN)
