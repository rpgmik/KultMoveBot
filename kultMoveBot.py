## Runs in Linux via: python kultTarotBot.py
## Requires Python > 3.4
## Bot needs to be given message read and send permissions on the Discord server.
## Need to install the discord.py API wrapper (e.g., via: pip install discord.py)

import random
import discord
import yaml
from discord.utils import get
from discord.ext import commands
from datetime import datetime

description = 'Kult Move Bot'
bot = commands.Bot(command_prefix='!', description=description)

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

with open('./all_moves.yml', 'r') as stream:
  moves = yaml.safe_load(stream)

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

@bot.event
async def on_ready():
    print(bot.user.id)
    print(bot.user.name)
    print('---------------')
    print('This bot is ready for action!')

@bot.command(pass_context=True)
async def move(ctx, *args):

    if len(args)==0:
        dice = '```md\n'
        dice += "Please specify a Move (or use '!move ?' for help)"
        dice += '```'

    else:
        bits = [x.lower() for x in args]

        if bits[0] in ["?", "help"]:
            dice = '```md\n'
            dice += help
            dice += '```'

        elif bits[0] in ["info"]:
            ## Collect server install info
            dice = "**Currently running on " + str(len(bot.guilds)) + " Discord servers.**\n"
            dice += "Code available at: \n"
            dice += "<https://github.com/rpgmik/KultMoveBot>"
            dice += "\n"
            dice += "To add the bot to your server: \n"
            dice += "<https://discordapp.com/api/oauth2/authorize?client_id=625741456082206740&permissions=0&scope=bot>"
            dice += "\n"
            dice += "Discord server for bot support issues: \n"
            dice += "<https://discord.gg/fE7AVtm9Yu>"
            
        elif bits[0] not in list(moves):
            dice = '```md\n'
            dice += 'Please specify a Move (or "!move ?" for help)'
            dice += '```'

        elif bits[0] in list(moves):

            try:
                roll = [random.randint(1,10), random.randint(1,10)]

                options = moves[bits[0]]

                result = roll[0] + roll[1]
                mod = ''

                # Add mofifier to dice
                if len(bits) > 1:
                    mod = [' ',list(bits[1])[0],' ',list(bits[1])[1],' ']
                    mod = gap.join(mod)
                    if list(bits[1])[0]=="+":
                        result = result + int(list(bits[1])[1])
                    elif list(bits[1])[0]=="-":
                        result = result - int(list(bits[1])[1])

                # Determine outcome
                if result < 10:
                    outcome = options[3]
                elif result > 14:
                    outcome = options[1]
                else:
                    outcome = options[2]

                # Format data for output
                dice = '```md\n'
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

                # Collect move data for saving
                guild = get(ctx.message.guild.name)                                
                dt = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
                saveDat =  str(dt)
                saveDat += ", " + str(ctx.message.guild.id)
                saveDat += ", " + ctx.message.guild.name
                saveDat += ", " + ctx.message.content
                saveDat += ", " + str(roll[0]) + " + " + str(roll[1])
                if len(bits) > 1:
                   saveDat += ' ' + list(bits[1])[0] + ' ' + list(bits[1])[1]
                saveDat += ", " + str(result) + "\n"

                ## Write to file
                with open('info.txt','a') as file:
                    file.write(saveDat)
            
            except Exception:
                dice = '```md\n'
                dice += "Error with move synatx (type '!move ?' for help)"
                dice += '```'

    ## Send message to channel
    await ctx.send(dice)

if __name__ == '__main__':
    try:
        bot.run(TOKEN)
    except Exception as e:
        print('Could Not Start Bot')
        print(e)
    finally:
        print('Closing Session')
        session.close()

bot.run(TOKEN)