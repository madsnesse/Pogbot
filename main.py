import discord
from random import Random

client = discord.Client()
TOKEN = ""
with open("token.txt", "r") as f:
    TOKEN = f.read()
responses = ["quite poggers indeed", "p-ordet","poggerino my dude", "thats indeed pretty p-word", "p0000g!", "90Ԁ","kinda sus tho"]

rand = Random()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if "pog" in message.content.lower() or "p0g" in message.content.lower() or "pøg" in message.content.lower() or "pög" in message.content.lower() or "p-ordet" in message.content.lower():
        foundEmoji = False
        emojis = []
        for emo in client.emojis:
            if "pog" in emo.name.lower():
                foundEmoji = True
                emojis.append(emo)
        if foundEmoji and rand.randint(0,len(emojis)+1)!=1:
            await message.add_reaction(rand.choice(emojis))
            
        else:
            await message.add_reaction("🅿️")
            await message.add_reaction("🅾️")
            await message.add_reaction("🇬")
        await message.channel.send(rand.choice(responses))

client.run(TOKEN)