import discord
from discord.ext import commands
import json
from random import choice
import os


token = 'NjA5MDE1NDY4MTQ5MzA5NDU5.XUwkDQ.YC5xBj29LXD7oQ6ccp9o_MY0UTw'
bot = commands.Bot(command_prefix='!')

def band_img():
    DIR = 'C:\\Users\\magge\\Desktop\\Atom\\Artists\\'
    img = choice(os.listdir(DIR))
    return (DIR + '\\' + img)

@bot.event
async def on_ready():
    print("Dictionary open!")

@bot.command()
async def band(ctx,*,arg):
    DIR = 'C:\\Users\\magge\\Desktop\\Atom\\Bands\\'+arg+'.txt'
    json_file = open(DIR, "r", encoding="utf-8")
    band = json.load(json_file)
    json_file.close()
    await ctx.send(band)

@bot.command()
async def img_band(ctx):
    await ctx.send(file=discord.File(band_img()))

bot.run(token)
