# KultMoveBot - version 2.0
Python Discord bot for "move rolls" in the roleplaying game KULT: Divinity Lost.

### UPGRADED TO VERSION 2.0: 7 MAY 2020

- See below for usage instructions.
- Huge thanks to Frost for taking on the mammoth task of extracting and formatting ALL of the Kult moves for use here.

###  Kult discord server:

- KULT: Elysium https://discord.gg/QmRB2qN
 
### Bugs
- none yet!
- Ping me (\@mik) on the above server if you notice any bot issues...

### Feature requests
- they will come...

### Installation

Install into a discord server (you will need admin privileges) via:

https://discordapp.com/api/oauth2/authorize?client_id=625741456082206740&permissions=0&scope=bot

### Instructions 

Once the bot is installed, typing

`
!move ?
`

in Discord will produce the Usage message below.

#### Usage:

```
!move ? - displays this message
!move help - displays this message
!move info - displays bot code info
!move xxx - roll to perform Move xxx
!move xxx -1 - roll to perform Move xxx with negative modifier -1
!move xxx +2 - roll to perform Move xxx with positive modifier +2
```

#### Moves:

```
- Use the full move name (lower-case, no spaces) when rolling.
  For example, to roll for 'Artistic Talent' with a +2 bonus use:
  !move artistictalent +2
- Shortcuts are available for commonly used moves (see below).
  For example, to roll for 'Avoid Harm' with a +1 bonus use:
  !move ah +1
```

#### Move shortcuts:

```
- Avoid Harm (ah): roll + Reflexes
- Endure Injury (ei): roll + Fortitude - Harm (+ Armour)
- Keep It Together (kit): roll + Willpower
- Act Under Pressure (aup): roll + Coolness
- Engage In Combat (eic): roll + Violence
- Influence Other - NPC (ion): roll + Charisma
- Influence Other - PC (iop): roll + Charisma
- See Through the Illusion (sti): roll + Soul
- Read A Person (rap): roll + Intuition
- Observe A Situation (oas): roll + Perception
- Investigate (inv): roll + Reason
- Help Or Hinder (hoh): roll + Attribute
- Non-standard move (non): roll + Modifier
```

#### Anomalies (full move name):

```
- Influence Other - NPC: !move influenceothernpc
- Influence Other - PC: !move influenceotherpc
```
