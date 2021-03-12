import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == "client.user":
    return
  if "$" in (message.content)[0]:
    if str(message.author) == "Pranav#0828":
      if (message.content[1:5]=="give"):
        
        await message.channel.send(message.content[6:])
      else:
        await message.channel.send(":/")
        
    else:
      await message.channel.send("You are not authorized to give brownie points")
      print(message.author)
    
    #elif "harish" in message.content.lower():
    #    print("hi")
    #    message.channel.send()

client.run(os.getenv("TOKEN"))