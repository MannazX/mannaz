import discord
from discord.ext import commands
import random
from random import choice
import os, os.path
import http.client
import json

client = commands.Bot(command_prefix='!')

def Get_gif():
    DIR = 'C:\\Users\\magge\\Desktop\\Atom\\samuel_gf\\'
    gif = choice(os.listdir(DIR))
    return (DIR + '\\' + gif)

def gif_roast():
    DIR = 'C:\\Users\\magge\\Desktop\\Atom\\mp_roast\\'
    gif = choice(os.listdir(DIR))
    return (DIR + '\\' + gif)

def gif_shooting():
    DIR = 'C:\\Users\\magge\\Desktop\\Atom\\sam_shoot\\'
    gif = choice(os.listdir(DIR))
    return (DIR + '\\' + gif)

def chuck_norris_joke():
    conn = http.client.HTTPSConnection("matchilling-chuck-norris-jokes-v1.p.rapidapi.com")
    # https://rapidapi.com/matchilling/api/chuck-norris
    headers = {
        'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
        'x-rapidapi-key': "1aece3393emsh73ca8dfe0f5722dp1dc8fbjsn6ad8250ba066",
        'accept': "application/json"
        }

    conn.request("GET", "/jokes/random", headers=headers)

    res = conn.getresponse()
    data = res.read()

    #print(data.decode("utf-8"))
    chuck_norris = data.decode("utf-8")
    chuck_norris = json.loads(chuck_norris)
    for chuck in chuck_norris:
        if chuck == "value":
            joke = chuck_norris[chuck]
    return joke

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='I shot you!'))
    print("Samuel in the house mofo!")

@client.command(aliases=['resp'])
async def sam_response(ctx, *, question):
    response = ['Sit down! Before I sit you down!', 'Check out the big brain of Brad here!', 'Does he look like a bitch?', 'English, motherfucker, do you speak it?', 'This is an A and a B conversation C your way out of this',
                '..and I shall strike down upon thee with great vengeance and furious anger!', 'Fuck you!', 'Shut the fuck up!', 'AK-47, the very best there is.', 'I eat every motherfucking thing', 'Everything I touch turns to shit',
                'What this situation requires is a lot more of you shutting your goddammed mouth', 'Oh my god, why!?', 'Say what again, I dare you, I double dare you motherfucker, say what again',
                'Im so tired of these motherfucking snakes on this motherfucking train!', 'Thats how I roll motherfucker!', 'No!', 'What part of shut the fuck up do you not understand?', 'I dont need your attitude, I have one of my own', 'Maybe you should just stop trying',
                'Have you got any idea of who you are talking to?', 'Excuse me! Excuse me!', 'Wait, what the fuck did you just say?', 'Does it look just a little bit like I give a fuck?', 'Yes you did! Yes you did!', 'You got mail motherfucker!', 'Hell yeah!',
                'I have no idea, seriously, not a clue', 'I dont know what youre talking about, and Im not wasting my time trying to figure it out', 'What aint no country I ever heard off, do they speak English in What?!', 'Motherfucking bullshit is what this is', "Mhhhhhhm, that is a tasty burger!"]
    await ctx.send(f"{choice(response)}")

@client.command()
async def what(ctx):
    reply = {"1":"What ain't no country I ever heard of, they speak English in What?", "2":"English motherfucker, do you speak it?!", "3":"Say what again, I dare you, I double dare you motherfucker!", "4":gif_shooting()}
    list_reply = []
    for index in reply:
        list_reply.append(index)
    reply_choice = choice(list_reply)
    response = reply[reply_choice]
    if reply_choice == "4":
        response = "...when I lay my vengeance upon thee!"
        gif_resp = reply[reply_choice]
    await ctx.send(response); await ctx.send(file=discord.File(gif_resp))

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def sam(ctx):
    await ctx.send(file=discord.File(Get_gif()))

@client.command()
async def roast(ctx):
    await ctx.send(file=discord.File(gif_roast()))

@client.command()
async def chuck(ctx):
    await ctx.send(chuck_norris_joke())

@client.command()
async def sam_swears(ctx):
    await ctx.send("!myswears")

client.run('NTk0NzgwNzczNzkwNTE1MjEx.XRjY0Q.OalDUkXYCOQiQhNM2Xh0zmB1t-0')
