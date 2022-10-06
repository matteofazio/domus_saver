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


#class variables

host_capo = ['']
casa_ID = ['']
date_to = ['']
date_from = ['']

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
	await ctx.message.channel.send(f'Inzio salvataggio dell\'immagine')
        imageName = str(uuid.uuid4()) + '.jpg'
        r = requests.get(url, stream=True)
        with open(imageName,'wb',) as out_file:
            print('Saving image: ' + imageName)
            shutil.copyfileobj(r.raw, out_file)
            shutil.move(out_file, 'C:\\FAZIO\\Desktop\\QUESTURE',)
    await ctx.message.channel.send(f'Immagine Salvata!')


@client.command(name = 'casa')
async def casa(ctx):
	casa_ID = ['']
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	casa_ID.append(ctx.message.content[5:])
	await ctx.message.channel.send(f'Saved info about casa')


@client.command(name = 'da')
async def da(ctx):
	date_from = ['']
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return	
	date_from.append(ctx.message.content[3:])
	await ctx.message.channel.send(f'Salvata la data di check in')


@client.command(name = 'a')
async def a(ctx):
	date_to = ['']
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	date_to.append(ctx.message.content[2:])
	await ctx.message.channel.send(f'Salvata la data di check out')


@client.command(name = 'capo')
async def capo(ctx):
	host_capo = ['']
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	host_capo.append(ctx.message.content[5:])
	await ctx.message.channel.send(f'Saved info about capo')


@client.command(name = 'info')
async def info(ctx):
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	await ctx.message.channel.send(f'Capogruppo: {host_capo[-1]} \nCasa n°{casa_ID[-1]} \nData check-in: {date_from[-1]}\nData check-out:{date_to[-1]}')
	print(casa, host_capo, date_from, date_to)

@client.command(name = 'ID')
async def ID(ctx):
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	elenco_case = ['Via xxx = 1', 'Via yyy = 2']
	a = ''
	for i in elenco_case:
		a = a + i + '\n'
	await ctx.message.channel.send(a)


@client.command(name = 'comandi')
async def comandi(ctx):
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	elenco_comandi = ['a:   inserisci data check-out','capo:   dichiara se è il capogruppo', 'casa:   inserisci ID casa','da:   inserisci data check-in','info:   controlla i dati inseriti','ID:   richiedi ID case', 'save:   salva l\'immagine']
	b = ''
	for j in elenco_comandi:
		b = b + j + '\n'
	await ctx.message.channel.send(b)

@client.event
async def on_ready():
    print("Bot is ready")

client.run(os.environ['DISCORD_TOKEN_discord'])
