import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
       await client.send_message(message.channel, 'Pong!')

client.run('NzUyNzM4MDA2ODI1MzA0MTE2.X1b_5g.ZMAgAK937r5phr-OnVRDkI1n1_o')
