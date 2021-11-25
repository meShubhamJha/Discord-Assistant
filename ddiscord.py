from asyncio import events
import discord 
import os

from discord import channel
from test import database
from linkFind import giveSong

client = discord.Client()
db = database()

    

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  

@client.event
async def on_message(message, ctx):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('$HELP'):
        print(message.author)
        if str(message.author) == "Avalanche#2431" or str(message.author) == "Maut_ka_saudagar#5740":
            print("sattsts")
            await message.channel.send("Enter the info in following manner\n$ADD name;role;email;username\nDo not include space before or after ;")
    
    elif msg.startswith('$ADD'):
        if str(message.author) == "Avalanche#2431" or str(message.author) == "Maut_ka_saudagar#5740":
            raw = str(msg)[5:].split(";")
            db.addUser(str(raw[0]), str(raw[1]), str(raw[2]), str(raw[3]))
            await message.channel.send("Added Successfully")
    
    elif msg.startswith('$play'):
        if not ctx.message.author.voice:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
            return
        else:
            channel = ctx.message.author.voice.channel
        await channel.connect()
        if str(message.author) == "Avalanche#2431" or str(message.author) == "Maut_ka_saudagar#5740":
            raw = str(msg)[6:]
            if "/" in raw:
                song = giveSong(raw.split("/")[0], raw.split("/")[1])
                print(raw.split("/")[0], raw.split("/")[1])
            else:
                song = giveSong(raw)
            destination = client.get_channel(795968552544895026)
            await destination.send(song)
            await message.channel.send("Playing your song in hydra")




token = "Nzk2MzM5Nzk1MjIyNTkzNTQ2.X_WfOg.csDHmya8xFw-Lp-aGH7839jMZ7Q"
client.run(token)



