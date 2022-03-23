import asyncpraw
import discord
from random import choice
from senhas import token, senhaReddit #aqui vão suas credenciais do reddit/token discord

reddit = senhaReddit #aqui vai as informações da API do reddit https://github.com/reddit-archive/reddit/wiki/OAuth2

client = discord.Client()

@client.event
async def on_ready(): #carrega os links dos subreddits/conecta o bot
    memes = await reddit.subreddit("whatswrongwithyourdog")  # carrega o subreddit
    memes2 = await reddit.subreddit("tinder")
    imagem = ([meme async for meme in memes.top("year", limit=1000)])#armazena 1000 links em um array
    print (len(imagem))#apenas pra ver quantos links carrega
    imagem2 = ([meme2 async for meme2 in memes2.top("year", limit=1000)])
    print (len(imagem2))#apenas pra ver quantos links carrega
    global geral #para conseguir usar em outras funções
    geral = imagem+imagem2 #soma dos dois arrays para poder randomizar a imagem enviada pelo bot
    print('{0.user} Conectado normalmente'.format(client))#avisa que o bot carregou

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!imagem'):
        a = choice(geral)
        print (a.url)
        await message.channel.send(a.url)

client.run(token) #token do discord https://discord.com/developers/docs/intro
