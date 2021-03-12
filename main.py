import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == "client.user":
        return

    print(message.author) 
    
    #elif "harish" in message.content.lower():
    #    print("hi")
    #    message.channel.send()

client.run('')
