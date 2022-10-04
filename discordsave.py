import discord
from discord.ext import commands
import os
import asyncio
import requests
from requests import get
from time import time
from pandas import DataFrame, to_datetime, concat
from datetime import datetime
import uuid
import shutil



client = discord.Client(intents=discord.Intents.all())

#ID channel

carta_identità_italia_nuova = 1022173249855029384
casa = []
host_capo = []

@client.event
async def on_connect():
	channel = client.get_channel(carta_identità_italia_nuova)
	await channel.send('Mi sono connesso ora!')

@client.event
async def on_message(message):
	if message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {message.content}')
	if message.author == client.user:
		return
	if message.content[:4]=="casa":
		casa.append(message.content)
		await message.channel.send(f'Saved info about casa')
	elif message.content[:4]=="capo":
		host_capo.append(message.content)
		await message.channel.send(f'Saved info about capo')
	elif message.content == 'save' or message.content == 'Starting ...' or message.content == 'Saved!' or message.content == 'Mi sono connesso ora!':
		return
	else:
		host_capo.append('')
		await message.channel.send(f'Messaggio errato! \nSe si vuole salvare la casa digitare: casa ... \nSe si vuole salvare il soggetto come capo digitare: capo ...')
	print(casa, host_capo)

@client.event
async def on_ready():
    print("Bot is ready")



client.run(os.environ['DISCORD_TOKEN_discordsave'])
