#Build an embed from JSON data

import datetime
import discord
import re

def embedFromJson(raw, ping):
    raw["description"] = re.sub(r'{ping}', ping, raw["description"])
    embed = discord.Embed(\
        description = raw["description"],\
        type = "rich",\
        timestamp = datetime.datetime.now(),\
        color = raw["color"])
    embed.set_footer(\
        text = raw["footer"]["text"],\
        icon_url = raw["footer"]["url"])
    embed.set_image(url = raw["url"])
    return embed;