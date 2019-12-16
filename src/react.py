#React to a command

import json

from globalvars import *
import embedfromjson

def react(commandRaw, context):
    ping = 'bruh'

    command = commandRaw.split(' ', 1)[0]

    with open("reactionPresets/" + command + ".json", "r") as f:
        presetRaw = json.loads(f.read())

        if presetRaw["nsfw"] and not(context.channel.is_nsfw()):
            return discord.Embed(title = "Oops!", type = "rich", description = "This command can only be used on NSFW channels.", color = 0xFF0000)

        if presetRaw["requiresPing"] and (len(context.mentions) == 0):
            return discord.Embed(title = "Oops!", type = "rich", description = "This command needs you to ping someone.", color = 0xFF0000)

        if presetRaw["randomizeImage"]:
            #randomize image tm
            pass

        if presetRaw["requiresPing"]:
            ping = context.mentions[0].mention

        return embedfromjson.embedFromJson(presetRaw["baseMessage"], ping)