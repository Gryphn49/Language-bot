#language-bot

import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print("client.user.id")
    print("-------")

@client.event
async def on_message(message):
    if message.content.startswith("\ping"):
        await client.send_message(message.channel, "It hast workeded.")

client.run("Your_Token_Here")
