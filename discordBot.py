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
    try:
        url = ctx.message.attachments[0].url
    except IndexError:
        print("Error : No attachments")
        await ctx.send("No attachments detected")
    else:
        imageName = str(uuid.uuid4()) + '.jpg'
        r = requests.get(url, stream=True)
        with open(imageName,'wb',) as out_file:
            print('Saving image: ' + imageName)
            shutil.copyfileobj(r.raw, out_file)
            shutil.move(out_file, 'C:\\FAZIO\\Desktop\\QUESTURE')


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


client.run(os.environ['DISCORD_TOKEN_discord'])
