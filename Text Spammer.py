import discord
import asyncio
import random

bot1 = discord.Client()
bot2 = discord.Client()
bot3 = discord.Client()
client = discord.Client()

token1 = 'add spammer token here'
token2 = 'add spammer token here'
token3 = 'add spammer token here'

arr = ["the","okok","of","and","a","to","in","is","you","that","it","he","was","for","on","are",]

@client.event
async def on_message(message):
  
  channel = message.channel
  
  if message.guild.id != add serevr id here:
   if message.author.id != 571027211407196161:
    return
  embed = message.embeds
  try:
    embed = embed[0]
  except:
    return
  embed = embed.footer
  message = str(embed.text)
  if message.startswith('Type'):
    message = message.split()
    number = message[2]
    await channel.send(f'.claim {number}')

@bot1.event
async def on_ready():
  while True:
    channel = bot1.get_channel(add channel id here)
    word = random.choice(arr)
    await channel.send(word)
    await asyncio.sleep(3)

@bot2.event
async def on_ready():
  while True:
    channel = bot2.get_channel(add channel id here)
    word = random.choice(arr)
    await channel.send(word)
    await asyncio.sleep(3)

@bot3.event
async def on_ready():
  while True:
    channel = bot3.get_channel(add channel id here)
    word = random.choice(arr)
    await channel.send(word)
    await asyncio.sleep(3)

loop = asyncio.get_event_loop()
loop.create_task(bot1.start(token1, bot=False))
loop.create_task(bot2.start(token2, bot=False))
loop.create_task(bot3.start(token3, bot=False))

loop.run_forever()