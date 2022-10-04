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
casa = []
host_capo = []


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


@client.command(name = 'info')
async def info(ctx):
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	if ctx.message.content[5:9]=="casa":
		casa.append(ctx.message.content)
		await ctx.message.channel.send(f'Saved info about casa')
	elif ctx.message.content[5:9]=="capo":
		host_capo.append(ctx.message.content)
		await ctx.message.channel.send(f'Saved info about capo')
	elif ctx.message.content == 'Starting ...' or ctx.message.content == 'Saved!' or ctx.message.content == 'Mi sono connesso ora!':
		return
	else:
		host_capo.append('')
		await ctx.message.channel.send(f'Messaggio errato! \nSe si vuole salvare la casa digitare: casa ... \nSe si vuole salvare il soggetto come capo digitare: capo ...')
	print(casa, host_capo)


@client.event
async def on_ready():
    print("Bot is ready")


client.run('MTAyMjE3OTExNzE1MzY2NTA1NQ.G5Xy9C.IbSqFUHsn7_G3F6vu9Kr6CCNUHrzaXYgNITHYg')
