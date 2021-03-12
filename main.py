import discord
import os
from replit import db

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == "client.user":
    return
  if "$" in (message.content)[0]:
    if (message.content[1:5]=="give"):
      if str(message.author) == "Pranav#0828":
          try:
            db[message.content[6:]] += 10
          except:
            db[message.content[6:]] = 10
          # db[message.content[6:]] = db[message.content[6:]] + 10
          await message.channel.send(str(message.content[6:])+" has a balance of "+str(db[message.content[6:]])+" brownie points.")
      else:
        await message.channel.send("You are not authorized to give brownie points")
    elif message.content[1:5]=="":
      pass
    #elif "harish" in message.content.lower():
    #    print("hi")
    #    message.channel.send()

client.run(os.getenv("TOKEN"))