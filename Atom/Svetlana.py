# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:28:31 2019

@author: magge
"""
#import numpy as np
# import matplotlib.pyplot as plt
import http.client
import discord
from discord.ext import commands
import random
from random import choice
import json
import os
from urllib import request
import math as m

def gif():
    DIR = 'C:\\Users\\magge\\Desktop\\Atom\\Russian_luxury\\'
    gif = choice(os.listdir(DIR))
    return (DIR + '\\' + gif)

def sassy_socialist_meme():
    DIR = 'C:\\Users\\magge\\Desktop\\Atom\\Sassy_socialist_memes\\'
    gif = choice(os.listdir(DIR))
    return (DIR + '\\' + gif)

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("Bot ready")

# @bot.command()
# async def dibbity(ctx):
#     await ctx.send(f"dabbity - {round(bot.latency * 1000)}ms")

@client.command()
async def weather(ctx,*,arg):
    city = arg
    country_code = 'dk'
    API_KEY = 'de9b7989fd101af413a7dd3d80913a39'
    link = 'http://api.openweathermap.org/data/2.5/weather?q='+city+','+country_code+'&appid='+API_KEY
    resp = request.urlopen(link)
    data = resp.read()
    json_str = data.decode("UTF-8")
    weather = json.loads(json_str)
    conv_kelv = 273.15
    weather.update({'main': {'temp':m.ceil(291.75-conv_kelv)}})
    del weather["coord"]; del weather["weather"][0]["id"]; del weather["weather"][0]["icon"]; del weather["base"]; del weather["visibility"]; del weather["clouds"]; del weather["dt"]; del weather["sys"]; del weather["timezone"]; del weather["id"]; del weather["name"]; del weather["cod"]
    await ctx.send(weather)

@client.command()
async def slav_food(ctx):
    await ctx.send(file=discord.File(gif()))

@client.command()
async def russian(ctx,*,arg):
    DIR = 'C:\\Users\\magge\\Desktop\\Atom\\Russian_vocab_json-format\\'+arg+'.txt'
    json_file = open(DIR, 'r', encoding="utf-8")
    word_list = json.load(json_file)
    json_file.close()
    translation = []
    for index in word_list:
        translation.append([word_list[index]])
        for i in range(len(translation)):
            word_list.update({index:translation[i]})
    await ctx.send(word_list)

# @client.command()
# async def lama(ctx,*,arg):
#     DIR = 'C:\\Users\\magge\\Desktop\\Atom\\Mattek_3\\Lama\\'+arg
#     img = choice(os.listdir(DIR))
#     await ctx.send(file=discord.File(sassy_socialist_meme())

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


@client.command()
async def ss_meme(ctx):
    await ctx.send(file=discord.File(sassy_socialist_meme()))


#url_object = urllib.request('https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random')
#dict = json.load(url_object)

#@client.command(aliases=['chuck'])
#async def chuck_norris(ctx):
#    await ctx.send(dict)

client.run('NTkzMzcxOTg3OTAwODkxMTU3.XRM66g.0qLLKEN6WRrGjAL8sApC9t_WoBg')
