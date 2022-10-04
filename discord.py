import discord
from discord.ext import commands
import os
import asyncio
from requests import get
from time import time
from pandas import DataFrame, to_datetime, concat
from datetime import datetime
import uuid
import requests
import shutil



client = commands.Bot(command_prefix='', intents=discord.Intents.all())

#ID channels

carta_identità_italia_nuova = 1022173249855029384


@client.event
async def on_connect():
	channel = client.get_channel(carta_identità_italia_nuova)
	await channel.send('Mi sono connesso ora!')

@client.command(name = 'save')
async def save(ctx):
	print('Saving ...')
	await ctx.message.channel.send(f'Starting ...')
	imageName = str(uuid.uuid4()) + '.jpg'
	await ctx.message.attachments[0].save(imageName)
	await ctx.message.channel.send(f'Saved!')

@client.event
async def on_ready():
    print("Bot is ready")


client.run(os.environ['DISCORD_TOKEN'])
