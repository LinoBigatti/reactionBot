# ReactionBot
## A discord bot for reactions

### Running the bot
This assumes an ubuntu-like terminal is used.

First, install python and the required packages:
```Bash
sudo apt-get install python3
sudo apt-get install python3-pip
pip3 install -r requirements.txt
```

Then, add the bot token on ``config.json``.

At last, run the launcher:
```Bash
./Launcher.sh
```

### Creating new reactions
The bot uses reaction presets, found on the reactionPresets/ folder, named <commandName>.json. One of them looks like this:

```json
{
  "nsfw": false,
  "requiresPing": false,
  "randomizeImage": false,
  "baseMessage": {
  	"description": "reaction text",
  	"url": "image url",
  	"color": embedcolor,
  	"footer": {
  		"text": "footer text",
  		"url": "footer image url"
  	}
  }
}
```

#### nsfw
Dictates if the command can be used outside of NSFW channels. Can be ``true`` or ``false``.

#### requiresPing
Dictates if the command requires an user to be pinged. Can be ``true`` or ``false``.

#### randomizeImage
Dictates if the command uses a randomized image url. Can be ``true`` or ``false``.

#### baseMessage
##### description
The embed text. String.
##### url
The embed image url. String. Only use if not using randomized images.
##### color
The embed color. Decimal number, convert from 0xRRGGBB.
##### footer
###### text
The footer text. String.
###### url
The footer image url. String.

### Randomizing images.
To randomize images, you just need to add a file named <commandName>.txt on the gfx/ folder. It should look like this:

```
http://images6.fanpop.com/image/photos/34000000/Gumi-vocaloids-and-utauloids-34045123-800-800.jpg
https://static.zerochan.net/GUMI.full.1048349.jpg
```

Theres one line for each url.