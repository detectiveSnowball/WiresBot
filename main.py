import discord
import os
import time

client = discord.Client()


@client.event
async def on_ready():

  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if (message.author == client.user):
    return

  if (message.content.lower().startswith("wires")):
    time.sleep(2.5)
    await message.channel.send('meow.')

client.run(os.getenv('TOKEN'))
