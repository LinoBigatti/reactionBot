#Load the config

import json

token = ""
prefix = ""

with open("config.json", "r") as f:
    raw = json.loads(f.read())
    token = raw["token"]
    prefix = raw["prefix"]