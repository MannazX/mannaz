import discord
from discord.ext import commands
import random
from random import choice
import os


def tarot_pic():
    DIR = 'C:\\Users\\magge\\Desktop\\Atom\\Tarot\\'
    gif = choice(os.listdir(DIR))
    return (DIR + '\\' + gif)


client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='A game with your life'))
    print("Ready to rumble!")

@client.command(aliases=['dice'])
async def regular_dice(ctx):
    roll = random.randint(1,6)
    await ctx.send(f"Outcome of dice roll: {roll}")

@client.command(aliases=['20dice'])
async def _20_dice(ctx):
    roll = random.randint(1,20)
    await ctx.send(f"Outcome of 20 sided dice roll: {roll}")

@client.command(aliases=['coin'])
async def coinflip(ctx):
    sides = ['head', 'tail']
    flip = random.choice(sides)
    await ctx.send(flip)

@client.command(aliases=['meyer'])
async def roll(ctx):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    roll4 = random.randint(1,6)
    await ctx.send(f"Your roll:{roll1},{roll2}. My roll:{roll3},{roll4}")

@client.command()
async def play_dice(ctx,*,N=10):
    your_rolls = []
    bot_rolls = []
    for i in range(N):
        your_roll = random.randint(1,6)
        your_rolls.append(your_roll)
        bot_roll = random.randint(1,6)
        bot_rolls.append(bot_roll)
    your_sum = sum(your_rolls)
    bot_sum = sum(bot_rolls)
    if your_sum > bot_sum:
        end_statement = "You win!"
    elif your_sum < bot_sum:
        end_statement = "I win!"
    else:
        end_statement = "It's a draw!"
    await ctx.send(f"Your rolls are: {your_rolls}, the sum is {your_sum}. My rolls are: {bot_rolls}, the sum is {bot_sum}. {end_statement}")

@client.command()
async def list_dice(ctx, *, N=10):
   list = []
   for i in range(N):
       ran = random.randint(1,6)
       list.append(ran)
   await ctx.send(list)

@client.command()
async def draw(ctx, *, N=10):
    options = [i for i in cards]
    your_draws = []
    bot_draws = []
    your_score = 0
    bot_score = 0
    end_statement = []
    for i in range(N):
        your_draw = random.choice(options)
        your_draw_rank = 0
        bot_draw_rank = 0
        bot_draw = random.choice(options)
        for i in cards:
            if your_draw == i:
                your_draw_rank += cards[i]
            if bot_draw == i:
                bot_draw_rank += cards[i]
        if your_draw_rank > bot_draw_rank:
            your_score += 1
        elif bot_draw_rank > your_draw_rank:
            bot_score += 1
        your_draws.append(your_draw)
        bot_draws.append(bot_draw)
    if your_score > bot_score:
        end_statement = "You win!"
    elif your_score < bot_score:
        end_statement = "I win!"
    else:
        end_statement = "It's a draw!"
    await ctx.send(f"Your draws: {your_draws}, your score: {your_score}. My draws: {bot_draws}, my score: {bot_score}. {end_statement}")


@client.command()
async def tarot(ctx):
    tarot_deck = {"The World (Downright)":-21, "Judgement (Downright)":-20, "The Sun (Downright)":-19, "The Moon (Downright)":-18, "The Star (Downright)":-17, "The Tower (Downright)":-16, "The Devil (Downright)":-15, "Temperance (Downright)":-14, "Death (Downright)":-13, "The Hanged Man (Downright)":-12, "Justice (Downright)":-11, "The Wheel of Fortune (Downright)":-10, "The Hermit (Downright)":-9, "Strength (Downright)":-8, "The Chariot (Downright)":-7, "The Lovers (Downright)":-6, "The Heirophant (Downright)":-5, "The Emperor (Downright)":-4, "The Empress (Downright)":-3, "The High Priestess (Downright)":-2, "The Magician (Downright)":-1, "The Fool (Downright)":0, "The Fool (Upright)": 0, "The Magician (Upright)":1, "The High Priestess (Upright)":2, "The Empress (Upright)":3, "The Emperor (Upright)":4, "The Heirophant (Upright)":5, "The Lovers (Upright)":6, "The Chariot (Upright)":7, "Strength (Upright)":8, "The Hermit (Upright)":9, "The Wheel of Fortune (Upright)":10, "Justice (Upright)":11, "The Hanged Man (Upright)":12, "Death (Upright)":13, "Temperance (Upright)":14, "The Devil (Upright)":15, "The Tower (Upright)":16, "The Star (Upright)":17, "The Moon (Upright)":18, "The Sun (Upright)":19, "Judgement (Upright)":20, "The World (Upright)":21}
    cards = [rank for rank in tarot_deck]
    your_draw = choice(cards)
    your_rank = 0
    bot_draw = choice(cards)
    bot_rank = 0
    for i in tarot_deck:
        if your_draw == i:
            your_rank += tarot_deck[i]
        elif bot_draw == i:
            bot_rank += tarot_deck[i]
    rank_sum = your_rank + bot_rank
    if rank_sum > 0:
        end_statement = "You Win!"
    elif rank_sum < 0:
        end_statement = "I win!"
    else:
        end_statement = "It's a draw!"
    await ctx.send(f"Your draw is: {your_draw}, the value is: {your_rank}. My draw is: {bot_draw}, the value is: {bot_rank}. The sum is {rank_sum}, {end_statement}")

@client.command()
async def draw_tarot(ctx):
    await ctx.send(file=discord.File(tarot_pic()))

@client.command()
async def sum_99(ctx):
    cards = [i for i in card_deck]
    my_draws = []
    bot_draws = []
    my_sum = 0
    bot_sum = 0
    total_sum = 0
    while total_sum < 99:
        for my_card in card_deck:
            my_draw = choice(cards)
            my_draws.append(my_draw)
            if my_draw == my_card:
                my_draw = choice(cards)
                my_draws.append(my_draw)
                my_sum += card_deck[my_card]
        for bot_card in card_deck:
            bot_draw = choice(cards)
            bot_draws.append(bot_draw)
            if bot_draw == bot_card:
                bot_draw = choice(cards)
                bot_draws.append(bot_draw)
                bot_sum += card_deck[bot_card]
            total_sum = (my_sum + bot_sum)
    if len(my_draws) > len(bot_draws):
        statement = "You lose"
    elif len(bot_draws) > len(my_draws):
        statement = "I lose"
    await ctx.send(f"The sum is: {total_sum}, {statement}")

#game needs refinement.

# @client.command()
# async def sum_99(ctx):
#     card_deck = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
#     cards = [i for i in card_deck]
#     my_draws = []
#     bot_draws = []
#     card_sum = 0
#     while card_sum < 99:
#         for card in card_deck:
#             my_draw = choice(cards)
#             my_draws.append(my_draw)
#             if my_draw == card:
#                 card_sum += card_deck[card]
#             bot_draw = choice(cards)
#             bot_draws.append(bot_draw)
#             if bot_draw == card:
#                 card_sum += card_deck[card]
#     if len(my_draws) > len(bot_draws):
#         statement = "You lose"
#     else:
#         statement = "I lose"
#     await ctx.send(f"The sum is {card_sum}, the length of your list is {len(my_draws)}, the length of my list is {len(bot_draws)}. {statement}")

client.run('NTk3NDkxNjYwMDE2MDU4Mzg4.XSI3zg.XPbdy9favqrQ15nNNmiVgL9k32A')
