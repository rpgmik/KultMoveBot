## Runs in Linux via: python kultTarotBot.py
## Requires Python > 3.4
## Bot needs to be given message read and send permissions on the Discord server.
## Need to install the discord.py API wrapper (e.g., via: pip install discord.py)

import random
import discord
import all_moves
from discord.utils import get
from datetime import datetime

## Ascertain mode: dev or production
m = open('modeFile.txt', "r")
MODE = m.readline().rstrip()
m.close()

## Read in Discord bot token from file
if MODE=="prod":
    tokenFile = 'prodToken.txt'
elif MODE=="dev":
    tokenFile = 'devToken.txt'

f = open(tokenFile, "r")
TOKEN = f.readline().rstrip()
f.close()

## Define variables here...

sep = ' '
gap = ''

moves = all_moves.moves

help=""

help += "# Usage:\n"
help += "!move ? - displays this message\n"
help += "!move help - displays this message\n"
help += "!move info - displays bot support info\n"
help += "!move xxx - roll to perform Move xxx\n"
help += "!move xxx -1 - roll to perform Move xxx with negative modifier -1\n"
help += "!move xxx +2 - roll to perform Move xxx with positive modifier +2\n"
help += "# Moves:\n"
help += "- Use the full move name (lower-case, no spaces) when rolling.\n"
help += "  For example, to roll for 'Artistic Talent' with a +2 bonus use:\n" 
help += "  !move artistictalent +2\n"
help += "- Shortcuts are available for commonly used moves (see below).\n"
help += "  For example, to roll for 'Avoid Harm' with a +1 bonus use:\n"
help += "  !move ah +1\n"
help += "# Move shortcuts:\n"
help += "- Avoid Harm (ah): roll + Reflexes\n"
help += "- Endure Injury (ei): roll + Fortitude - Harm (+ Armour)\n"
help += "- Keep It Together (kit): roll + Willpower\n"
help += "- Act Under Pressure (aup): roll + Coolness\n"
help += "- Engage In Combat (eic): roll + Violence\n"
help += "- Influence Other - NPC (ion): roll + Charisma\n"
help += "- Influence Other - PC (iop): roll + Charisma\n"
help += "- See Through the Illusion (sti): roll + Soul\n"
help += "- Read A Person (rap): roll + Intuition\n"
help += "- Observe A Situation (oas): roll + Perception\n"
help += "- Investigate (inv): roll + Reason\n"
help += "- Help Or Hinder (hoh): roll + Attribute\n"
help += "- Non-standard move (non): roll + Modifier\n"
help += "# Anomalies (full move name):\n"
help += "- Influence Other - NPC: !move influenceothernpc\n" 
help += "- Influence Other - PC: !move influenceotherpc\n" 

## Get discord connection
client = discord.Client()

## Define an event so that Bot can read messages
@client.event
async def on_message(message):

    ## Bot info
    info=""
    # info += "**KultMoveBot**\n"
    ## Collect server install info
    info += "**Currently running on " + str(len(list(client.guilds))) + " Discord servers.**\n"
    info += "Code available at: \n"
    info += "<https://github.com/rpgmik/KultMoveBot>"
    info += "\n"
    info += "To add the bot to your server: \n"
    info += "<https://discordapp.com/api/oauth2/authorize?client_id=625741456082206740&permissions=0&scope=bot>"
    info += "\n"
    info += "Discord server for bot support issues: \n"
    info += "<https://discord.gg/fE7AVtm9Yu>"
    ## Converts move command to lowercase, making it
    ## case insensitive
    message.content=message.content.lower()

    ## Respond if user sends "!move"
    if message.content.startswith('!move'):

        ## Split into into "!move", the type of Move to undertake, the modifier (if any), and a comment (if any).
        bits = message.content.split(" ")

        dice = '```md\n'
        if len(bits)==1:
            dice += "Please specify a Move (or use '!move ?' for help)"

        if len(bits)>1:
            if bits[1] in ["?", "help"]:
                dice += help

            elif bits[1] in ["info"]:
                dice += ""

            elif bits[1] not in moves:
                dice += 'Please specify a Move (or "!move ?" for help)'

            elif bits[1] in moves:
                roll = [random.randint(1,10), random.randint(1,10)]

                #Instead of going by case to case basis, think about how easy it is to add moves now
                options = moves[bits[1]]

                result = roll[0] + roll[1]
                mod = ''

                guild = get(message.guild.name)
                
                # print(message.guild.id)
                # print(message.guild.name)
                
                dt = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

                # print(dt)
                
                saveDat =  str(dt)
                saveDat += ", " + str(message.guild.id)
                saveDat += ", " + message.guild.name
                saveDat += ", " + message.content
                saveDat += ", " + str(roll[0]) + " + " + str(roll[1])

                if len(bits) > 2:
                    mod = [' ',list(bits[2])[0],' ',list(bits[2])[1],' ']
                    mod = gap.join(mod)
                    saveDat += ' ' + list(bits[2])[0] + ' ' + list(bits[2])[1]
                    if list(bits[2])[0]=="+":
                        result = result + int(list(bits[2])[1])
                    elif list(bits[2])[0]=="-":
                        result = result - int(list(bits[2])[1])

                saveDat += ", " + str(result) + "\n"

                ## Write to file
                with open('info.txt','a') as file:
                    file.write(saveDat)

                if result < 10:
                    outcome = options[3]
                elif result > 14:
                    outcome = options[1]
                else:
                    outcome = options[2]

                dice += options[0]
                dice += "\nResult: "
                dice += str(roll[0])
                dice += " + "
                dice += str(roll[1])
                dice += mod
                dice += " = "
                dice += str(result)
                dice += "\nOutcome: "
                dice += outcome

        dice += '```'

        if bits[1] in ["info"]:
            dice = info

        ## Send message to channel
        await message.channel.send(dice)

## Write login details locally (i.e., on linux box where bot code is running)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Kult: !move ? for help"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("Installed on",len(list(client.guilds)), "guilds:")
    for s in list(client.guilds):
        print("- " + s.name)
    print('------')

## Run Bot on Discord server
client.run(TOKEN)
