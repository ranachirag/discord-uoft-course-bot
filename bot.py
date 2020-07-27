import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import scraper

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
async def find(ctx, course):
    response = scraper.course_info(course)
    await ctx.send(response)

@client.command(name='prereq', help='Gives prerequisites of course requested')
async def prereq(ctx, course):
    response = scraper.course_prereq(course)
    await ctx.send(response)

@client.command(name='name', help='Gives name of course requested')
async def name(ctx, course):
    response = scraper.course_name(course)
    await ctx.send(response)

@client.command(name='description', help='Gives description of course requested')
async def description(ctx, course):
    response = scraper.course_descrip(course)
    await ctx.send(response)

@client.command(name='breadth', help='Gives breadth requirements of course requested')
async def breadth(ctx, course):
    response = scraper.course_breadth(course)
    await ctx.send(response)

@client.command(name='exclusions', help='Gives exclusions of course requested')
async def exclusion(ctx, course):
    response = scraper.course_exclu(course)
    await ctx.send(response)

client.run(TOKEN)
