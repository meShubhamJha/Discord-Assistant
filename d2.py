import discord
from discord import message
import discord.ext.commands as commands
from discord.ext import commands,tasks
from test import database
from linkFind import giveSong
db = database()


intents = discord.Intents().all()
client = discord.Client(intents=intents)

token = "Nzk2MzM5Nzk1MjIyNTkzNTQ2.X_WfOg.csDHmya8xFw-Lp-aGH7839jMZ7Q"


bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

@bot.command(name='hello', description="Greet the user!")
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")


@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):

    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!play'):
        await message.channel.send('Starting to play')
        raw = str(message.content)[6:]
        if "/" in raw:
            song = giveSong(raw.split("/")[0], raw.split("/")[1])
            print(raw.split("/")[0], raw.split("/")[1])
        else:
            song = giveSong(raw)
       
        await message.channel.send(song)
        destination = bot.get_channel(795968552544895026)
        await destination.send(song)
    await bot.process_commands(None)

bot.run(token)

