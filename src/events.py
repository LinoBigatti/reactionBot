#Handle events.

import discord

import config
import react
from globalvars import *

@bot.event
async def on_ready():
    print("Started bot.")
    print("Bot info:")
    print(bot.user.name)
    print(bot.user.id)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.bot:
        return

    if message.content.startswith(config.prefix):
        command = message.content[len(config.prefix):]
        await message.channel.send(embed=react.react(command, message))