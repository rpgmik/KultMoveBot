## Runs in Linux via: python kultTarotBot.py
## Requires Python > 3.4
## Bot needs to be given message read and send permissions on the Discord server.
## Need to install the discord.py API wrapper (e.g., via: pip install discord.py)

import random
import discord

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

ah = ['# Avoid Harm', ' You emerge completely unharmed.', 'You avoid the worst of it, but the GM decides if you end up in a bad spot, lose something, or partially sustain Harm.', 'You were too slow to react or you made a bad judgment call. Perhaps you didn’t avoid any Harm at all, or you ended up in an even worse spot than before. The GM makes a Move.']

ei = ['# Endure Injury', ' You ride out the pain and keep going.', 'You are still standing, but the GM picks one condition:\n - The injury throws you off balance.\n - You lose something.\n - You receive a Serious Wound.', 'The injury is overwhelming. You choose if you\n - Are knocked out (the GM may also choose to inflict a Serious Wound).\n - Receive a Critical Wound, but may continue to act (if you already have a Critical Wound, you may not choose this option again).\n - Die.']

kit = ['# Keep It Together', ' You grit your teeth and stay the course.', 'The effort to resist instills a condition, which remains with you until you have time to recuperate. You get -1 in situations where this condition would be a hinderance to you. Choose one:\n - You become angry (−1 Stability).\n - You become sad (−1 Stability).\n - You become scared (−1 Stability).\n - You become guilt-ridden (−1 Stability).\n - You become obsessed (+1 Relation to whatever caused the condition).\n - You become distracted (−2 in situations where the condi- tion limits you).\n - You will be haunted by the experience at a later time.', 'The strain is too much for your mind to handle. The GM chooses your reaction:\n - cower powerless in the threat’s presence\n - panic with no control of your actions\n - suffer emotional trauma (−2 Stability)\n - suffer life-changing trauma (−4 Stability).']

aup = ['# Act Under Pressure', 'You do what you intended.', 'You do it, but hesitate, are delayed, or must deal with a complication – the GM reveals an unexpected outcome, a high price, or a difficult choice.', 'There are serious consequences, you make a mistake, or you’re exposed to the danger. The GM makes a Move.']

eic = ['# Engage In Combat', 'You inflict damage to your opponent and avoid counterattacks.', 'You inflict damage, but at a cost. The GM chooses one:\n - You’re subjected to a counterattack.\n - You do less damage than intended.\n - You lose something important.\n - You expend all your ammo.\n - You’re beset by a new threat.\n - You’ll be in trouble later on.', 'Your attack doesn’t go as anticipated. You might be subjected to bad luck, miss your target, or pay a high price for your assault. The GM makes a Move.']

ion = ['# Influence Other (NPC)', 'She does what you ask', 'She does what you ask, but the GM chooses one:\n - She demands better compensation.\n - Complications will arise at a future time.\n - She gives in for the moment, but will change her mind and regret it later.', 'Your attempt has unintended repercussions. The GM makes a Move. ']

iop = ['# Influence Other (PC)', 'Both options below:\n - She’s motivated to do what you ask, and recieves +1 for her next roll, if she does it.\n - She’s worried of the consequences if she doesn’t do what you ask, and gets −1 Stability if she doesn’t do it.', 'Choose one option below:\n - She’s motivated to do what you ask, and recieves +1 for her next roll, if she does it.\n - She’s worried of the consequences if she doesn’t do what you ask, and gets −1 Stability if she doesn’t do it.', 'The character gets +1 on her next roll against you. The GM makes a Move.']

sti = ['# See Through The Illusion', 'You perceive things as they truly are.', 'You see Reality, but you also affect the Illusion. The GM chooses one:\n - Something senses you.\n - The Illusions tears around you.', 'The GM explains what you see and makes a Move.']

rap = ['# Read A Person', 'You may ask two questions:\n - Are you lying?\n - How do you feel right now?\n - What are you about to do?\n - What do you wish I would do?\n - How could I get you to ______?', 'You may ask one question:\n - Are you lying?\n - How do you feel right now?\n - What are you about to do?\n - What do you wish I would do?\n - How could I get you to ______?', 'You accidentally reveal your own intentions to the person you’re trying to read. Tell the GM/player what these intentions are. The GM makes a Move.']

oas = ['# Observe A Situation', 'Ask two questions:\n - What is my best way through this?\n - What currently poses the biggest threat? ◊ What can I use to my advantage?\n - What should I be on the lookout for?\n - What is being hidden from me?\n - What seems strange about this?', 'Ask one question:\n - What is my best way through this?\n - What currently poses the biggest threat?\n - What can I use to my advantage?\n - What should I be on the lookout for?\n - What is being hidden from me?\n - What seems strange about this?', 'You get to ask a question anyway, but you get no bonus for it and miss something, attract unwanted attention or expose yourself to danger. The GM makes a Move.']

inv = ['# Investigate', 'Ask two questions:\n - How can I find out more about what I’m investigating?\n - What is my gut feel about what I’m investigating?\n - Is there anything weird about what I’m investigating?', 'You may ask one question:\n - How can I find out more about what I’m investigating?\n - What is my gut feel about what I’m investigating?\n - Is there anything weird about what I’m investigating?\nThe information comes at a cost, determined by the GM, such as requiring someone or something for the answer, exposing yourself to danger, or needing to expend extra time or resources. Will you do what it takes?', 'You may get some information anyway, but you pay a price for it. You may expose yourself to dangers or costs. The GM makes a Move.']

hoh = ['# Help Or Hinder', 'You may modify the subsequent roll by +2/−2.', 'You may modify the subsequent roll by +1/−1.', 'Your interference has unintended consequences. The GM makes a Move.']

moves = ["ah", "ei", "kit", "aup", "eic", "ion", "iop", "sti", "rap",
"oas", "inv", "hoh"]

## Get discord connection
client = discord.Client()

## Define an event so that Bot can read messages
@client.event
async def on_message(message):

    ## Respond if user sends "!move"
    if message.content.startswith('!move'):

        ## Split into into "!move", the type of Move to undertake, the modifier (if any), and a comment (if any).
        bits = message.content.split(" ")

        dice = '```md\n'
        if len(bits)==1:
            dice += "Please specify a Move"

        if len(bits)>1:
            if bits[1] in ["?", "help"]:
                dice += "# Usage:\n"
                dice += "!move ? - displays this message\n"
                dice += "!move help - displays this message\n"
                dice += "!move xxx - roll to perform Move xxx\n"
                dice += "!move xxx -1 - roll to perform Move xxx with negative modifier -1\n"
                dice += "!move xxx +2 - roll to perform Move xxx with positive modifier +2\n"
                dice += "# Moves:\n"
                dice += "- Avoid Harm (ah): roll + Reflexes\n"
                dice += "- Endure Injury (ei): roll + Fortitude - Harm (+ Armour)\n"
                dice += "- Keep It Together (kit): roll + Willpower\n"
                dice += "- Act Under Pressure (aup): roll + Coolness\n"
                dice += "- Engage In Combat (eic): roll + Violence\n"
                dice += "- Influence Other - NPC (ion): roll + Charisma\n"
                dice += "- Influence Other - PC (iop): roll + Charisma\n"
                dice += "- See Through the Illusion (sti): roll + Soul\n"
                dice += "- Read A Person (rap): roll + Intuition\n"
                dice += "- Observe A Situation (oas): roll + Perception\n"
                dice += "- Investigate (inv): roll + Reason\n"
                dice += "- Help Or Hinder (hoh): roll + Attribute\n"

            elif bits[1] not in moves:
                dice += 'Please specify a Move (or "!move ?" for help)'

            elif bits[1] in moves:
                roll = [random.randint(1,10), random.randint(1,10)]
                if bits[1] == "ah":
                    options = ah
                if bits[1] == "ei":
                    options = ei
                if bits[1] == "kit":
                    options = kit
                if bits[1] == "aup":
                    options = aup
                if bits[1] == "eic":
                    options = eic
                if bits[1] == "ion":
                    options = ion
                if bits[1] == "iop":
                    options = iop
                if bits[1] == "sti":
                    options = sti
                if bits[1] == "rap":
                    options = rap
                if bits[1] == "oas":
                    options = oas
                if bits[1] == "inv":
                    options = inv
                if bits[1] == "hoh":
                    options = hoh

                result = roll[0] + roll[1]
                mod = ''

                if len(bits) > 2:
                    mod = [' ',list(bits[2])[0],' ',list(bits[2])[1],' ']
                    mod = gap.join(mod)
                    if list(bits[2])[0]=="+":
                        result = result + int(list(bits[2])[1])
                    elif list(bits[2])[0]=="-":
                        result = result - int(list(bits[2])[1])

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

        ## Send message to channel
        await message.channel.send(dice)

## Write login details locally (i.e., on linux box where bot code is running)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Alas: !move ? for help"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

## Run Bot on Discord server
client.run(TOKEN)
