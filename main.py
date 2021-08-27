import discord
import os
import time
import pet


client = discord.Client()


@client.event
async def on_ready():

  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if (message.author == client.user):
    return

  if "wires" in message.content.lower():
    time.sleep(2.5)
    await message.channel.send('meow')

  if "genshin" in message.content.lower() or "impact" in message.content.lower():
    time.sleep(1.5)
    await message.channel.send("*hissssssssssssss*")

  if "food" in message.content.lower() and "genshin" not in message.content.lower() and "impact" not in message.content.lower():
    time.sleep(2.5)
    await message.channel.send("(*runs towards you for snack!*)")

  if "meow" in message.content.lower():
    time.sleep(2.5)
    await message.channel.send("meow")





client.run(os.getenv('TOKEN'))
