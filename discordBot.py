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
from pathlib import Path


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
        imageName = str(Path.home() / Path(str(uuid.uuid4()) + '.jpg'))
        #imageName = str(uuid.uuid4()) + '.jpg'
        r = requests.get(url, stream=True)
        with open(imageName,'wb',) as out_file:
            print('Saving image: ' + imageName)
            shutil.copyfileobj(r.raw, out_file)
            out_file.close()
            shutil.move(imageName,'C:\\FAZIO\\Documents\\GitHub\\domus_saver\\'+str(uuid.uuid4()) + '.jpg')
        await ctx.message.channel.send(f'Immagine Salvata!')


@client.command(name = 'casa')
async def casa(ctx):
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	if len(casa_ID) > 50:
		casa_ID.pop(0)
	casa_ID.append(ctx.message.content[5:])
	await ctx.message.channel.send(f'Saved info about casa')
	print(casa_ID, host_capo, date_from, date_to)


@client.command(name = 'da')
async def da(ctx):
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return	
	if len(date_from) > 50:
		date_from.pop(0)
	date_from.append(ctx.message.content[3:])
	await ctx.message.channel.send(f'Salvata la data di check in')
	print(casa_ID, host_capo, date_from, date_to)


@client.command(name = 'a')
async def a(ctx):
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	if len(date_to) > 50:
		date_to.pop(0)
	date_to.append(ctx.message.content[2:])
	await ctx.message.channel.send(f'Salvata la data di check out')
	print(casa_ID, host_capo, date_from, date_to)


@client.command(name = 'capo')
async def capo(ctx):
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	if len(host_capo) > 50:
		host_capo.pop(0)
	host_capo.append(ctx.message.content)
	await ctx.message.channel.send(f'Saved info about capo')
	print(casa_ID, host_capo, date_from, date_to)


@client.command(name = 'non_capo')
async def non_capo(ctx):
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	if len(host_capo) > 50:
		host_capo.pop(0)
	host_capo.append('')
	await ctx.message.channel.send(f'Saved info about capo')
	print(casa_ID, host_capo, date_from, date_to)


@client.command(name = 'info')
async def info(ctx):
	if ctx.message.channel.id==carta_identità_italia_nuova:
		print(f'Messaggio: {ctx.message.content}')
	if ctx.message.author == client.user:
		return
	await ctx.message.channel.send(f'Capogruppo: {host_capo[-1]} \nCasa n°{casa_ID[-1]} \nData check-in: {date_from[-1]}\nData check-out:{date_to[-1]}')
	print(casa_ID, host_capo, date_from, date_to)

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
	elenco_comandi = ['a:   inserisci data check-out','capo:   dichiara se è il capogruppo', 'non_capo:   dichiara se non è il capogruppo' ,'casa:   inserisci ID casa','da:   inserisci data check-in','info:   controlla i dati inseriti','ID:   richiedi ID case', 'save:   salva l\'immagine']
	b = ''
	for j in elenco_comandi:
		b = b + j + '\n'
	await ctx.message.channel.send(b)

@client.event
async def on_ready():
    print("Bot is ready")


client.run(os.environ['DISCORD_TOKEN_discord'])
