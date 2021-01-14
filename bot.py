import discord
from discord.ext import commands

client = commands.Bot(command_prefix="+")

@client.event
async def on_ready():
    print(" ")
    print("-------------------------------")
    print("Bot Online")
    print('Logged In As: ',client.user.name)
    print('ID: ',client.user.id)
    print('Discord Version: ',discord.__version__)
    print('-------------------------------')
    print(" ")
    print(" ")

@client.command()
async def globalleaderboards(ctx):
    await ctx.send("https://www.chess.com/players")

@client.command()
async def chessrules(ctx):
    await ctx.send("https://www.chess.com/learn-how-to-play-chess")

client.token("")