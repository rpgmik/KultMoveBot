

moves ={
'ah' : ['# Avoid Harm', ' You emerge completely unharmed.', 'You avoid the worst of it, but the GM decides if you end up in a bad spot, lose something, or partially sustain Harm.', 'You were too slow to react or you made a bad judgment call. Perhaps you didn’t avoid any Harm at all, or you ended up in an even worse spot than before. The GM makes a Move.']

,'ei' : ['# Endure Injury', ' You ride out the pain and keep going.', 'You are still standing, but the GM picks one condition:\n - The injury throws you off balance.\n - You lose something.\n - You receive a Serious Wound.', 'The injury is overwhelming. You choose if you\n - Are knocked out (the GM may also choose to inflict a Serious Wound).\n - Receive a Critical Wound, but may continue to act (if you already have a Critical Wound, you may not choose this option again).\n - Die.']

,'kit' : ['# Keep It Together', ' You grit your teeth and stay the course.', 'The effort to resist instills a condition, which remains with you until you have time to recuperate. You get -1 in situations where this condition would be a hinderance to you. Choose one:\n - You become angry (−1 Stability).\n - You become sad (−1 Stability).\n - You become scared (−1 Stability).\n - You become guilt-ridden (−1 Stability).\n - You become obsessed (+1 Relation to whatever caused the condition).\n - You become distracted (−2 in situations where the condition limits you).\n - You will be haunted by the experience at a later time.', 'The strain is too much for your mind to handle. The GM chooses your reaction:\n - cower powerless in the threat’s presence\n - panic with no control of your actions\n - suffer emotional trauma (−2 Stability)\n - suffer life-changing trauma (−4 Stability).']

,'aup' : ['# Act Under Pressure', 'You do what you intended.', 'You do it, but hesitate, are delayed, or must deal with a complication – the GM reveals an unexpected outcome, a high price, or a difficult choice.', 'There are serious consequences, you make a mistake, or you’re exposed to the danger. The GM makes a Move.']

,'eic' : ['# Engage In Combat', 'You inflict damage to your opponent and avoid counterattacks.', 'You inflict damage, but at a cost. The GM chooses one:\n - You’re subjected to a counterattack.\n - You do less damage than intended.\n - You lose something important.\n - You expend all your ammo.\n - You’re beset by a new threat.\n - You’ll be in trouble later on.', 'Your attack doesn’t go as anticipated. You might be subjected to bad luck, miss your target, or pay a high price for your assault. The GM makes a Move.']

,'ion' : ['# Influence Other (NPC)', 'She does what you ask', 'She does what you ask, but the GM chooses one:\n - She demands better compensation.\n - Complications will arise at a future time.\n - She gives in for the moment, but will change her mind and regret it later.', 'Your attempt has unintended repercussions. The GM makes a Move. ']

,'iop' : ['# Influence Other (PC)', 'Both options below:\n - She’s motivated to do what you ask, and recieves +1 for her next roll, if she does it.\n - She’s worried of the consequences if she doesn’t do what you ask, and gets −1 Stability if she doesn’t do it.', 'Choose one option below:\n - She’s motivated to do what you ask, and recieves +1 for her next roll, if she does it.\n - She’s worried of the consequences if she doesn’t do what you ask, and gets −1 Stability if she doesn’t do it.', 'The character gets +1 on her next roll against you. The GM makes a Move.']

,'sti' : ['# See Through The Illusion', 'You perceive things as they truly are.', 'You see Reality, but you also affect the Illusion. The GM chooses one:\n - Something senses you.\n - The Illusions tears around you.', 'The GM explains what you see and makes a Move.']

,'rap' : ['# Read A Person', 'You may ask two questions:\n - Are you lying?\n - How do you feel right now?\n - What are you about to do?\n - What do you wish I would do?\n - How could I get you to ______?', 'You may ask one question:\n - Are you lying?\n - How do you feel right now?\n - What are you about to do?\n - What do you wish I would do?\n - How could I get you to ______?', 'You accidentally reveal your own intentions to the person you’re trying to read. Tell the GM/player what these intentions are. The GM makes a Move.']

,'oas' : ['# Observe A Situation', 'Ask two questions:\n - What is my best way through this?\n - What currently poses the biggest threat?\n - What can I use to my advantage?\n - What should I be on the lookout for?\n - What is being hidden from me?\n - What seems strange about this?', 'Ask one question:\n - What is my best way through this?\n - What currently poses the biggest threat?\n - What can I use to my advantage?\n - What should I be on the lookout for?\n - What is being hidden from me?\n - What seems strange about this?', 'You get to ask a question anyway, but you get no bonus for it and miss something, attract unwanted attention or expose yourself to danger. The GM makes a Move.']

,'inv' : ['# Investigate', 'Ask two questions:\n - How can I find out more about what I’m investigating?\n - What is my gut feel about what I’m investigating?\n - Is there anything weird about what I’m investigating?', 'You may ask one question:\n - How can I find out more about what I’m investigating?\n - What is my gut feel about what I’m investigating?\n - Is there anything weird about what I’m investigating?\nThe information comes at a cost, determined by the GM, such as requiring someone or something for the answer, exposing yourself to danger, or needing to expend extra time or resources. Will you do what it takes?', 'You may get some information anyway, but you pay a price for it. You may expose yourself to dangers or costs. The GM makes a Move.']

,'hoh' : ['# Help Or Hinder', 'You may modify the subsequent roll by +2/−2.', 'You may modify the subsequent roll by +1/−1.', 'Your interference has unintended consequences. The GM makes a Move.']

,'avoidharm' : ['# Avoid Harm', ' You emerge completely unharmed.', 'You avoid the worst of it, but the GM decides if you end up in a bad spot, lose something, or partially sustain Harm.', 'You were too slow to react or you made a bad judgment call. Perhaps you didn’t avoid any Harm at all, or you ended up in an even worse spot than before. The GM makes a Move.']

,'endureinjury' : ['# Endure Injury', ' You ride out the pain and keep going.', 'You are still standing, but the GM picks one condition:\n - The injury throws you off balance.\n - You lose something.\n - You receive a Serious Wound.', 'The injury is overwhelming. You choose if you\n - Are knocked out (the GM may also choose to inflict a Serious Wound).\n - Receive a Critical Wound, but may continue to act (if you already have a Critical Wound, you may not choose this option again).\n - Die.']

,'keepittogether' : ['# Keep It Together', ' You grit your teeth and stay the course.', 'The effort to resist instills a condition, which remains with you until you have time to recuperate. You get -1 in situations where this condition would be a hinderance to you. Choose one:\n - You become angry (−1 Stability).\n - You become sad (−1 Stability).\n - You become scared (−1 Stability).\n - You become guilt-ridden (−1 Stability).\n - You become obsessed (+1 Relation to whatever caused the condition).\n - You become distracted (−2 in situations where the condition limits you).\n - You will be haunted by the experience at a later time.', 'The strain is too much for your mind to handle. The GM chooses your reaction:\n - cower powerless in the threat’s presence\n - panic with no control of your actions\n - suffer emotional trauma (−2 Stability)\n - suffer life-changing trauma (−4 Stability).']

,'actunderpressure' : ['# Act Under Pressure', 'You do what you intended.', 'You do it, but hesitate, are delayed, or must deal with a complication – the GM reveals an unexpected outcome, a high price, or a difficult choice.', 'There are serious consequences, you make a mistake, or you’re exposed to the danger. The GM makes a Move.']

,'engageincombat' : ['# Engage In Combat', 'You inflict damage to your opponent and avoid counterattacks.', 'You inflict damage, but at a cost. The GM chooses one:\n - You’re subjected to a counterattack.\n - You do less damage than intended.\n - You lose something important.\n - You expend all your ammo.\n - You’re beset by a new threat.\n - You’ll be in trouble later on.', 'Your attack doesn’t go as anticipated. You might be subjected to bad luck, miss your target, or pay a high price for your assault. The GM makes a Move.']

,'influenceothernpc' : ['# Influence Other (NPC)', 'She does what you ask', 'She does what you ask, but the GM chooses one:\n - She demands better compensation.\n - Complications will arise at a future time.\n - She gives in for the moment, but will change her mind and regret it later.', 'Your attempt has unintended repercussions. The GM makes a Move. ']

,'influenceotherpc' : ['# Influence Other (PC)', 'Both options below:\n - She’s motivated to do what you ask, and recieves +1 for her next roll, if she does it.\n - She’s worried of the consequences if she doesn’t do what you ask, and gets −1 Stability if she doesn’t do it.', 'Choose one option below:\n - She’s motivated to do what you ask, and recieves +1 for her next roll, if she does it.\n - She’s worried of the consequences if she doesn’t do what you ask, and gets −1 Stability if she doesn’t do it.', 'The character gets +1 on her next roll against you. The GM makes a Move.']

,'seethroughtheillusion' : ['# See Through The Illusion', 'You perceive things as they truly are.', 'You see Reality, but you also affect the Illusion. The GM chooses one:\n - Something senses you.\n - The Illusions tears around you.', 'The GM explains what you see and makes a Move.']

,'readaperson' : ['# Read A Person', 'You may ask two questions:\n - Are you lying?\n - How do you feel right now?\n - What are you about to do?\n - What do you wish I would do?\n - How could I get you to ______?', 'You may ask one question:\n - Are you lying?\n - How do you feel right now?\n - What are you about to do?\n - What do you wish I would do?\n - How could I get you to ______?', 'You accidentally reveal your own intentions to the person you’re trying to read. Tell the GM/player what these intentions are. The GM makes a Move.']

,'observeasituation' : ['# Observe A Situation', 'Ask two questions:\n - What is my best way through this?\n - What currently poses the biggest threat?\n - What can I use to my advantage?\n - What should I be on the lookout for?\n - What is being hidden from me?\n - What seems strange about this?', 'Ask one question:\n - What is my best way through this?\n - What currently poses the biggest threat?\n - What can I use to my advantage?\n - What should I be on the lookout for?\n - What is being hidden from me?\n - What seems strange about this?', 'You get to ask a question anyway, but you get no bonus for it and miss something, attract unwanted attention or expose yourself to danger. The GM makes a Move.']

,'investigate' : ['# Investigate', 'Ask two questions:\n - How can I find out more about what I’m investigating?\n - What is my gut feel about what I’m investigating?\n - Is there anything weird about what I’m investigating?', 'You may ask one question:\n - How can I find out more about what I’m investigating?\n - What is my gut feel about what I’m investigating?\n - Is there anything weird about what I’m investigating?\nThe information comes at a cost, determined by the GM, such as requiring someone or something for the answer, exposing yourself to danger, or needing to expend extra time or resources. Will you do what it takes?', 'You may get some information anyway, but you pay a price for it. You may expose yourself to dangers or costs. The GM makes a Move.']

,'helporhinder' : ['# Help Or Hinder', 'You may modify the subsequent roll by +2/−2.', 'You may modify the subsequent roll by +1/−1.', 'Your interference has unintended consequences. The GM makes a Move.']


,'non' : [
#name
'# Non-standard move'
, 

#success
'You succeed'
, 

#complications
'There are complications'
, 

#failure
'The GM makes a Move'
]







,'academicnetwork' : [
'# Academic Network'
,

' The person is a friend (Relation +1). '
,

' The person is an acquaintance (Relation +0). '
,

' You know one another, but there is an old enmity between the two of you (Relation +0). '
]



,'artistictalent' : [
'# Artistic Talent'
,

' Choose up to two options any time during the scene. \nOptions:\n'
+' - They want to see more of your art.\n'
+' - They are affected by the emotion you wanted to convey (e.g., anger, sorrow, fear, joy, lust, etc).\n'
+' - They look up to you (take +1 ongoing with the audience during this scene).\n'
+' - Their attention is fixed entirely on you throughout your performance. '
,

' Choose one option any time during the scene. \nOptions:\n'
+' - They want to see more of your art.\n'
+' - They are affected by the emotion you wanted to convey (e.g., anger, sorrow, fear, joy, lust, etc).\n'
+' - They look up to you (take +1 ongoing with the audience during this scene).\n'
+' - Their attention is fixed entirely on you throughout your performance. '
,

' Choose one option, but a complication/threat manifests. The GM makes a Move. \nOptions:\n'
+' - They want to see more of your art.\n'
+' - They are affected by the emotion you wanted to convey (e.g., anger, sorrow, fear, joy, lust, etc).\n'
+' - They look up to you (take +1 ongoing with the audience during this scene).\n'
+' - Their attention is fixed entirely on you throughout your performance. '
]



,'authority' : [
'# Authority'
,

' During this game session, choose up to three options. \nOptions:\n'
+' - Influence someone who has heard of your authority in your academic field, as if you had rolled a 15+.\n'
+' - Gain access to a university’s resources, such as their facilities, researchers, or scientific archives.\n'
+' - Make a statement about something or someone in mass media.\n'
+' - Gain access to people or places under the pretense of engaging in your research or studies. '
,

' During this game session, choose up to two options. \nOptions:\n'
+' - Influence someone who has heard of your authority in your academic field, as if you had rolled a 15+.\n'
+' - Gain access to a university’s resources, such as their facilities, researchers, or scientific archives.\n'
+' - Make a statement about something or someone in mass media.\n'
+' - Gain access to people or places under the pretense of engaging in your research or studies. '
,

' During this game session you may choose one option, but you also attract unwanted attention like stalkers, professional adversaries, competitors, or hostile forces. The GM makes a Move for them at some point during the session. \nOptions:\n'
+' - Influence someone who has heard of your authority in your academic field, as if you had rolled a 15+.\n'
+' - Gain access to a university’s resources, such as their facilities, researchers, or scientific archives.\n'
+' - Make a statement about something or someone in mass media.\n'
+' - Gain access to people or places under the pretense of engaging in your research or studies. '
]



,'awe-inspiring' : [
'# Awe-Inspiring'
,

' People around you accept you as their leader and listen to you. Take +1 ongoing against people in this scene. '
,

' People feel you’re leadership material and show you respect. Choose one of them, in particular, who goes along with what you think. You have +1 ongoing against them during this scene. '
,

' People feel like you’re the leader, but one of them tries to challenge you for it. The GM makes a Move. '
]



,'eliteeducation' : [
'# Elite Education'
,

' Choose up to three options. \nOptions:\n'
+' - Gain a favor from a country’s administration (e.g., released from jail, skip a customs check, or get help from the police).\n'
+' - Gain access to a location unavailable to the public.\n'
+' - Locate or track a hidden or missing person.\n'
+' - Receive both the means to escape and a safe hiding spot. '
,

' Choose up to two options. \nOptions:\n'
+' - Gain a favor from a country’s administration (e.g., released from jail, skip a customs check, or get help from the police).\n'
+' - Gain access to a location unavailable to the public.\n'
+' - Locate or track a hidden or missing person.\n'
+' - Receive both the means to escape and a safe hiding spot. '
,

' Choose one option, but you’ve become indebted to someone. The debt can be called in during the story, whenever the GM chooses. \nOptions:\n'
+' - Gain a favor from a country’s administration (e.g., released from jail, skip a customs check, or get help from the police).\n'
+' - Gain access to a location unavailable to the public.\n'
+' - Locate or track a hidden or missing person.\n'
+' - Receive both the means to escape and a safe hiding spot. '
]



,'erotic' : [
'# Erotic'
,

' Choose up to three options any time during this scene. \nOptions:\n'
+' - The person must have you, and will abandon their normally reasonable behavior to do so.\n'
+' - The person is distracted by you for as long as you’re in the vicinity, unable to concentrate on anything else.\n'
+' - The person becomes jealous of anyone competing for your attention, and tries to dispose of them by any means necessary.\n'
+' - You make them uncertain and confused. You take +1 ongoing against them during this scene. '
,

' Choose up to two options any time during this scene. \nOptions:\n'
+' - The person must have you, and will abandon their normally reasonable behavior to do so.\n'
+' - The person is distracted by you for as long as you’re in the vicinity, unable to concentrate on anything else.\n'
+' - The person becomes jealous of anyone competing for your attention, and tries to dispose of them by any means necessary.\n'
+' - You make them uncertain and confused. You take +1 ongoing against them during this scene. '
,

' Choose one option any time during this scene, but the nature of the attraction is different than you had hoped. The GM makes a Move. \nOptions:\n'
+' - The person must have you, and will abandon their normally reasonable behavior to do so.\n'
+' - The person is distracted by you for as long as you’re in the vicinity, unable to concentrate on anything else.\n'
+' - The person becomes jealous of anyone competing for your attention, and tries to dispose of them by any means necessary.\n'
+' - You make them uncertain and confused. You take +1 ongoing against them during this scene. '
]



,'fascination' : [
'# Fascination'
,

' Choose one option. \nOptions:\n'
+' - They are attracted to you.\n'
+' - They forget their woes when experiencing your art.\n'
+' - They are totally captivated by your art and forget all about their surrounding environment. '
,

' Choose one option, but the GM also chooses one of the following:\n'
+' - They become obsessed with you.\n'
+' - They want you right now. \nOptions:\n'
+' - They are attracted to you.\n'
+' - They forget their woes when experiencing your art.\n'
+' - They are totally captivated by your art and forget all about their surrounding environment. '
,

' They are affected by you in a way you didn’t anticipate, or the attraction is uncomfortably strong – you choose. The GM makes a Move. '
]



,'forkedtongue' : [
'# Forked Tongue'
,

' Choose one option:\n'
+' - They trust you (PC takes +1 Relation with you).\n'
+' - They’re spellbound by you (take +1 ongoing against them during this scene).\n'
+' - They reveal a weakness, which you can exploit later. '
,

' Choose one option from the list above, but there’s also a complication, chosen by the GM or player:\n'
+' - They see you as a friend they can turn to when in need.\n'
+' - They fall in love with you.\n'
+' - They will feel betrayed, spurned, humiliated, or manipulated whenever you abuse their trust in you. \nOptions:\n'
+' - They trust you (PC takes +1 Relation with you).\n'
+' - They’re spellbound by you (take +1 ongoing against them during this scene).\n'
+' - They reveal a weakness, which you can exploit later. '
,

' They see right through you and will act as they please. '
]



,'impostor' : [
'# Impostor'
,

' They can provide you with whatever you require. '
,

' One of them might be able to help, but it will take some convincing. '
,

' You know someone who can help, but they have already seen through your game. If you want their assistance it will require threats or blackmail to get them to provide it. '
]



,'influentialfriends' : [
'# Influential Friends'
,

' Your friends can arrange for what you want. '
,

' They can arrange for it, but you have to repay the favor later. '
,

' They arrange for what you want, but you get on a powerful person’s bad side or attract negative publicity. The GM makes a Move. '
]



,'moles' : [
'# Moles'
,

' You receive both options below. \nOptions:\n'
+' - The mole has penetrated the organization’s inner circle; however, their influence is limited.\n'
+' - The mole owes you one; however, you must meet their demands to get what you want. '
,

' Choose one of the options below. \nOptions:\n'
+' - The mole has penetrated the organization’s inner circle; however, their influence is limited.\n'
+' - The mole owes you one; however, you must meet their demands to get what you want. '
,

' The mole’s loyalties are questionable. Can you trust them? The GM makes a Move. '
]



,'networkofcontacts' : [
'# Network of Contacts'
,

' You may ask three questions from the list below. Questions:\n'
+' - What resources do they have at their disposal?\n'
+' - Who do they have business dealings with?\n'
+' - Where can I find them?\n'
+' - What do they want?\n'
+' - What are they most afraid of losing? '
,

' You may ask two questions from the list below. Questions:\n'
+' - What resources do they have at their disposal?\n'
+' - Who do they have business dealings with?\n'
+' - Where can I find them?\n'
+' - What do they want?\n'
+' - What are they most afraid of losing? '
,

' You may ask one question from the list below, but the person you’re inquiring about finds out you’re snooping around. The GM makes a Move. Questions:\n'
+' - What resources do they have at their disposal?\n'
+' - Who do they have business dealings with?\n'
+' - Where can I find them?\n'
+' - What do they want?\n'
+' - What are they most afraid of losing? '
]



,'notorious' : [
'# Notorious'
,

' They know of your reputation; you can decide what they have heard. The GM will have them act accordingly. You take +2 to your next roll to Infuence them. '
,

' They know of your reputation; you can decide what they have heard. '
,

' They know of your reputation; the GM decides what they have heard. '
]



,'perpetualvictim' : [
'# Perpetual Victim'
,

' Choose three options. You may save up to two options for use later during the scene. \nOptions:\n'
+' - Make someone want to take care of you.\n'
+' - Make an aggressive person want to not harm you.\n'
+' - Make someone confide in you. '
,

' Choose one option. \nOptions:\n'
+' - Make someone want to take care of you.\n'
+' - Make an aggressive person want to not harm you.\n'
+' - Make someone confide in you. '
,

' Someone tries to take advantage of you and your position. The GM makes a Move. '
]



,'seducer' : [
'# Seducer'
,

' Choose up to three options, useable any time in the story. \nOptions:\n'
+' - Give you something you want.\n'
+' - Reveal a secret.\n'
+' - Fight to protect you. NPCs who fall in love with you cannot oppose you, as long as you haven’t expended all your options. \n\nAgainst PCs, you may only choose the following options:\n'
+' - Make them feel bad for opposing you (they must Keep it Together)\n'
+' - They feel happy in your presence, and gain Stability (+2). '
,

' Choose up to two options, useable any time in the story. \nOptions:\n'
+' - Give you something you want.\n'
+' - Reveal a secret.\n'
+' - Fight to protect you. NPCs who fall in love with you cannot oppose you, as long as you haven’t expended all your options. \n\nAgainst PCs, you may only choose the following options:\n'
+' - Make them feel bad for opposing you (they must Keep it Together)\n'
+' - They feel happy in your presence, and gain Stability (+2). '
,

' Choose one option, useable any time in the story, but you also develop feelings for the person. Increase your Relation to them by +1. \nOptions:\n'
+' - Give you something you want.\n'
+' - Reveal a secret.\n'
+' - Fight to protect you. NPCs who fall in love with you cannot oppose you, as long as you haven’t expended all your options. \n\nAgainst PCs, you may only choose the following options:\n'
+' - Make them feel bad for opposing you (they must Keep it Together)\n'
+' - They feel happy in your presence, and gain Stability (+2). '
]



,'streetcontacts' : [
'# Street Contacts'
,

' Ask up to three questions. Questions:\n'
+' - What do you know about the [building/person/organization/ event]?\n'
+' - What rumors are circulating on the street at the moment?\n'
+' - How can I get into [location]?\n'
+' - Who in this city would know more about this supernatural thing? '
,

' Ask one question. Questions:\n'
+' - What do you know about the [building/person/organization/ event]?\n'
+' - What rumors are circulating on the street at the moment?\n'
+' - How can I get into [location]?\n'
+' - Who in this city would know more about this supernatural thing? '
,

' Ask one question, but someone becomes suspicious or aggressive. The GM makes a Move. Questions:\n'
+' - What do you know about the [building/person/organization/ event]?\n'
+' - What rumors are circulating on the street at the moment?\n'
+' - How can I get into [location]?\n'
+' - Who in this city would know more about this supernatural thing? '
]



,'streetwise' : [
'# Streetwise'
,

' No problem – you get what you’re after. Someone will fix you right up. '
,

' The GM chooses one option:\n'
+' - It will cost you something extra, such as in-kind services, tasks, or an inflated price.\n'
+' - You can get it handled, but only by dealing with someone you’re already indebted to.\n'
+' - “Shit, I had one, but I just let it go to [insert name] – maybe you can buy it from her?”\n'
+' - “Sorry, that’s a bit outside of my area, but maybe this will work instead?” '
,

' You think you find what you’re looking for, but there will be costly stipulations, considerable flaws, or major complications. The GM makes a Move. '
]



,'aceupthesleeve' : [
'# Ace up the Sleeve'
,

' Get 2 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - You have a small, concealed lethal weapon (stiletto or similar), which you can produce unnoticed.\n'
+' - You realize your opponent has a weakness you can exploit (take +2 to your next roll, if it involves exploiting the weakness). Ask the GM what it is.\n'
+' - You spot a way out. Ask the GM what it is. Take +2 to your next roll to make use of it. '
,

' Get 1 Edge. You may spend it at any time during the scene. \nEdges:\n'
+' - You have a small, concealed lethal weapon (stiletto or similar), which you can produce unnoticed.\n'
+' - You realize your opponent has a weakness you can exploit (take +2 to your next roll, if it involves exploiting the weakness). Ask the GM what it is.\n'
+' - You spot a way out. Ask the GM what it is. Take +2 to your next roll to make use of it. '
,

' Get 1 Edge, but the situation is worse than you imagined. The GM makes a Move. \nEdges:\n'
+' - You have a small, concealed lethal weapon (stiletto or similar), which you can produce unnoticed.\n'
+' - You realize your opponent has a weakness you can exploit (take +2 to your next roll, if it involves exploiting the weakness). Ask the GM what it is.\n'
+' - You spot a way out. Ask the GM what it is. Take +2 to your next roll to make use of it. '
]



,'backstab' : [
'# Backstab'
,

' Choose two options. \nOptions:\n'
+' - Aim for the sensitive parts: Deal +1 Harm.\n'
+' - Knock out: The NPC is rendered unconcious. PCs roll to Endure Injury and become neutralized on a –9.\n'
+' - Careful: You act soundlessly and, if your victim dies, you leave no clues or traces behind. '
,

' Choose one option. \nOptions:\n'
+' - Aim for the sensitive parts: Deal +1 Harm.\n'
+' - Knock out: The NPC is rendered unconcious. PCs roll to Endure Injury and become neutralized on a –9.\n'
+' - Careful: You act soundlessly and, if your victim dies, you leave no clues or traces behind. '
,

' You expose your betrayal and your target gets to react to your attack as usual. The GM makes a Move. '
]



,'boss' : [
'# Boss'
,

' They follow your orders and everything goes according to plan. '
,

' They follow your orders, but GM picks one option:\n'
+' - Someone got into trouble.\n'
+' - The job isn’t done, and needs something else to be completed.\n'
+' - There will be repercussions later on. '
,

' The GM decides what went wrong, and whether it’s immediately evident or will become apparent later on. The GM makes a Move. '
]



,'burglar' : [
'# Burglar'
,

' Get three options. You may spend them any time during the scene. \nOptions:\n'
+' - You silently open a locked door within a few moments.\n'
+' - You neutralize an alarm.\n'
+' - You bust a lockbox or safe in less than two minutes.\n'
+' - You avoid being discovered by someone.\n'
+' - Trick someone into believing you belong here (e.g., pretend you’re a security guard) for a limited time. '
,

' Get two options. You may spend them any time during the scene. \nOptions:\n'
+' - You silently open a locked door within a few moments.\n'
+' - You neutralize an alarm.\n'
+' - You bust a lockbox or safe in less than two minutes.\n'
+' - You avoid being discovered by someone.\n'
+' - Trick someone into believing you belong here (e.g., pretend you’re a security guard) for a limited time. '
,

' Get one option, but a problem arises. The GM makes a Move. \nOptions:\n'
+' - You silently open a locked door within a few moments.\n'
+' - You neutralize an alarm.\n'
+' - You bust a lockbox or safe in less than two minutes.\n'
+' - You avoid being discovered by someone.\n'
+' - Trick someone into believing you belong here (e.g., pretend you’re a security guard) for a limited time. '
]



,'driver' : [
'# Driver'
,

' Gain 3 Edges. You may spend them anytime during the scene. \nEdges:\n'
+' - Make a risky maneuver to get out of the way.\n'
+' - Shake off one pursuing vehicle.\n'
+' - Use your vehicle as a weapon against a pedestrian (2/3/4 Harm depending on speed).\n'
+' - Sideswipe another vehicle off the road. '
,

' Gain 2 Edges. You may spend them anytime during the scene. \nEdges:\n'
+' - Make a risky maneuver to get out of the way.\n'
+' - Shake off one pursuing vehicle.\n'
+' - Use your vehicle as a weapon against a pedestrian (2/3/4 Harm depending on speed).\n'
+' - Sideswipe another vehicle off the road. '
,

' Gain 1 Edge to spend any time during the scene, but the situation worsens somehow – maybe you speed past a police car, additional vehicles start pursuing you, or you or your vehicle is damaged. The GM makes a Move. \nEdges:\n'
+' - Make a risky maneuver to get out of the way.\n'
+' - Shake off one pursuing vehicle.\n'
+' - Use your vehicle as a weapon against a pedestrian (2/3/4 Harm depending on speed).\n'
+' - Sideswipe another vehicle off the road. '
]



,'escapeartist' : [
'# Escape Artist'
,

' You escape without complications. '
,

' You can choose to stay or escape at a cost, such as leaving something important behind or take something traceable with you. The GM decides what it is. '
,

' You are only half out the door when you’re caught in a really bad spot. The GM makes a Move. '
]



,'fasttalk' : [
'# Fast Talk'
,

' Choose two options. \nOptions:\n'
+' - Prevent the NPC from noticing something in her immediate vicinity.\n'
+' - Get the NPC to disclose something important (the GM will provide the details).\n'
+' - Distract the NPC. You take +1 to your next roll against them. '
,

' Choose one option. \nOptions:\n'
+' - Prevent the NPC from noticing something in her immediate vicinity.\n'
+' - Get the NPC to disclose something important (the GM will provide the details).\n'
+' - Distract the NPC. You take +1 to your next roll against them. '
,

' Choose one option, but they grow suspicious of your motives. The GM makes a Move. \nOptions:\n'
+' - Prevent the NPC from noticing something in her immediate vicinity.\n'
+' - Get the NPC to disclose something important (the GM will provide the details).\n'
+' - Distract the NPC. You take +1 to your next roll against them. '
]



,'icecold' : [
'# Ice Cold'
,

' Get 3 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Avoid an attack.\n'
+' - Manage to snatch something.\n'
+' - Maneuver into a better position.\n'
+' - Put someone in a bad position (everyone gets +2 to any attack Moves). '
,

' Get 2 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Avoid an attack.\n'
+' - Manage to snatch something.\n'
+' - Maneuver into a better position.\n'
+' - Put someone in a bad position (everyone gets +2 to any attack Moves). '
,

' Get 1 Edge, but you attract attention from the hostiles. The GM makes a Move. \nEdges:\n'
+' - Avoid an attack.\n'
+' - Manage to snatch something.\n'
+' - Maneuver into a better position.\n'
+' - Put someone in a bad position (everyone gets +2 to any attack Moves). '
]



,'improviser' : [
'# Improviser'
,

' Choose two options. \nOptions:\n'
+' - Come up with a convincing lie.\n'
+' - Find something you can use as a makeshift weapon (2 Harm chop/stab/crush).\n'
+' - Hide from a pursuer.\n'
+' - Set a trap that gives you a surprise advantage (+2 to your first attack Move). '
,

' Choose one option. \nOptions:\n'
+' - Come up with a convincing lie.\n'
+' - Find something you can use as a makeshift weapon (2 Harm chop/stab/crush).\n'
+' - Hide from a pursuer.\n'
+' - Set a trap that gives you a surprise advantage (+2 to your first attack Move). '
,

' Your improvisation makes the situation worse. The GM makes a Move. '
]



,'parkour' : [
'# Parkour'
,

' Choose two options. You may save one until later. \nOptions:\n'
+' - Scale a seemingly impossible obstacle.\n'
+' - Make a seemingly life-threatening leap without suffering Harm.\n'
+' - Successfully avoid a threat. '
,

' Choose one option. \nOptions:\n'
+' - Scale a seemingly impossible obstacle.\n'
+' - Make a seemingly life-threatening leap without suffering Harm.\n'
+' - Successfully avoid a threat. '
,

' Choose one option, but a complication, cost, or new threat emerges. The GM makes a Move. \nOptions:\n'
+' - Scale a seemingly impossible obstacle.\n'
+' - Make a seemingly life-threatening leap without suffering Harm.\n'
+' - Successfully avoid a threat. '
]



,'sneak' : [
'# Sneak'
,

' Get 2 options. You may spend them any time during the scene. \nOptions:\n'
+' - Find a secure hiding spot for a while.\n'
+' - Find an alternate route to avoid encountering people.\n'
+' - Bypass a security system or other obstacle without being noticed. '
,

' Get 1 option. You may spend them any time during the scene. \nOptions:\n'
+' - Find a secure hiding spot for a while.\n'
+' - Find an alternate route to avoid encountering people.\n'
+' - Bypass a security system or other obstacle without being noticed. '
,

' Get 1 option, but you manage to attract someone’s attention. The GM makes a Move. \nOptions:\n'
+' - Find a secure hiding spot for a while.\n'
+' - Find an alternate route to avoid encountering people.\n'
+' - Bypass a security system or other obstacle without being noticed. '
]



,'weaponmaster' : [
'# Weapon Master'
,

' You are a master of armed combat or gunplay. Choose your focus: Armed combat: Roll +Coolness instead of Violence to Engage in Combat in close quarters, as well as add the following options for close combat weapons:\n'
+' - Launching attack [2] [Distance: room]\n'
+' - Precision attack [2] [Distance: arm, ignores armor]\n'
+' - Tripping attack [2] [Distance: arm, targets falls prone] Gunplay: Roll +Coolness instead of Violence to Engage in Combat in a firefight, as well as add the following options:\n'
+' - Two shots in the chest and one in the head [4] [Distance: room, −2 ammo]\n'
+' - Disarm [1] [Distance: room, −1 ammo, a targeted PC must Act Under Pressure] '
,

' You are a master of armed combat or gunplay. Choose your focus: Armed combat: Roll +Coolness instead of Violence to Engage in Combat in close quarters, as well as add the following options for close combat weapons:\n'
+' - Launching attack [2] [Distance: room]\n'
+' - Precision attack [2] [Distance: arm, ignores armor]\n'
+' - Tripping attack [2] [Distance: arm, targets falls prone] Gunplay: Roll +Coolness instead of Violence to Engage in Combat in a firefight, as well as add the following options:\n'
+' - Two shots in the chest and one in the head [4] [Distance: room, −2 ammo]\n'
+' - Disarm [1] [Distance: room, −1 ammo, a targeted PC must Act Under Pressure] '
,

' You are a master of armed combat or gunplay. Choose your focus: Armed combat: Roll +Coolness instead of Violence to Engage in Combat in close quarters, as well as add the following options for close combat weapons:\n'
+' - Launching attack [2] [Distance: room]\n'
+' - Precision attack [2] [Distance: arm, ignores armor]\n'
+' - Tripping attack [2] [Distance: arm, targets falls prone] Gunplay: Roll +Coolness instead of Violence to Engage in Combat in a firefight, as well as add the following options:\n'
+' - Two shots in the chest and one in the head [4] [Distance: room, −2 ammo]\n'
+' - Disarm [1] [Distance: room, −1 ammo, a targeted PC must Act Under Pressure] '
]



,'animalspeaker' : [
'# Animal Speaker'
,

' Choose three options. You may save up to two for later. \nOptions:\n'
+' - Make the animal go against its instincts.\n'
+' - Make the animal follow you.\n'
+' - Make the animal protect you against an attacker. '
,

' Choose two options. You may save one for later. \nOptions:\n'
+' - Make the animal go against its instincts.\n'
+' - Make the animal follow you.\n'
+' - Make the animal protect you against an attacker. '
,

' Choose one option, but the animal is affected by your memories and Disadvantages. The GM makes a Move. \nOptions:\n'
+' - Make the animal go against its instincts.\n'
+' - Make the animal follow you.\n'
+' - Make the animal protect you against an attacker. '
]



,'chameleon' : [
'# Chameleon'
,

' Your disguise is convincing, as long as you keep the act going. '
,

' You manage to trick everyone who doesn’t examine you in detail, but choose one complication:\n'
+' - You can’t keep this deception up for very long. You must act fast, if you don’t want to risk getting exposed.\n'
+' - You leave traces and clues behind, which can be connected to you later on. '
,

' Your disguise is only effective at a distance. If you attract any attention to yourself, you will be exposed. '
]



,'characteractor' : [
'# Character Actor'
,

' Choose three options. You may save up to two for later. \nOptions:\n'
+' - Placate someone who is becoming suspicious.\n'
+' - Get access to a place outsiders aren’t allowed to go.\n'
+' - Get someone to tell you about this place’s secrets.\n'
+' - Get someone’s assistance with something here. '
,

' Choose two options. You may save one for later. \nOptions:\n'
+' - Placate someone who is becoming suspicious.\n'
+' - Get access to a place outsiders aren’t allowed to go.\n'
+' - Get someone to tell you about this place’s secrets.\n'
+' - Get someone’s assistance with something here. '
,

' Choose one option, but things don’t go according to plan. The GM makes a Move. \nOptions:\n'
+' - Placate someone who is becoming suspicious.\n'
+' - Get access to a place outsiders aren’t allowed to go.\n'
+' - Get someone to tell you about this place’s secrets.\n'
+' - Get someone’s assistance with something here. '
]



,'crafty' : [
'# Crafty'
,

' Choose up to two options. You may save one until later during this scene. \nOptions:\n'
+' - They become suspicious of someone else of your choosing.\n'
+' - They view you as their ally, for as long as you don’t betray them (+1 to all rolls against them).\n'
+' - They willingly do a favor for you. '
,

' Choose one option. \nOptions:\n'
+' - They become suspicious of someone else of your choosing.\n'
+' - They view you as their ally, for as long as you don’t betray them (+1 to all rolls against them).\n'
+' - They willingly do a favor for you. '
,

' They’re on to you. The GM makes a Move. '
]



,'extortionist' : [
'# Extortionist'
,

' Whenever you Read a Person, you may choose from these questions in addition to the usual ones:\n'
+' - What are you afraid of?\n'
+' - What is precious to you? '
,

' Whenever you Read a Person, you may choose from these questions in addition to the usual ones:\n'
+' - What are you afraid of?\n'
+' - What is precious to you? '
,

' Whenever you Read a Person, you may choose from these questions in addition to the usual ones:\n'
+' - What are you afraid of?\n'
+' - What is precious to you? '
]



,'interrogator' : [
'# Interrogator'
,

' Whenever you Read a Person and mention a name, person, or object, you may always ask “Are you lying?” This doesn’t count towards the number of questions you’re allowed to normally ask. '
,

' Whenever you Read a Person and mention a name, person, or object, you may always ask “Are you lying?” This doesn’t count towards the number of questions you’re allowed to normally ask. '
,

' Whenever you Read a Person and mention a name, person, or object, you may always ask “Are you lying?” This doesn’t count towards the number of questions you’re allowed to normally ask. '
]



,'intuitive' : [
'# Intuitive'
,

' You can sense people’s motives through subconscious readings of their body language, word choices, and behavior. Whenever you Read a Person, you may always ask one additional question, regardless of the outcome of your roll. '
,

' You can sense people’s motives through subconscious readings of their body language, word choices, and behavior. Whenever you Read a Person, you may always ask one additional question, regardless of the outcome of your roll. '
,

' You can sense people’s motives through subconscious readings of their body language, word choices, and behavior. Whenever you Read a Person, you may always ask one additional question, regardless of the outcome of your roll. '
]



,'observant' : [
'# Observant'
,

' Whenever you Read a Person, you may choose from these questions in addition to the usual ones:\n'
+' - What sort of person are you?\n'
+' - Is there anything odd about you? '
,

' Whenever you Read a Person, you may choose from these questions in addition to the usual ones:\n'
+' - What sort of person are you?\n'
+' - Is there anything odd about you? '
,

' Whenever you Read a Person, you may choose from these questions in addition to the usual ones:\n'
+' - What sort of person are you?\n'
+' - Is there anything odd about you? '
]



,'vigilant' : [
'# Vigilant'
,

' Whenever you Read a Person, you may choose from these questions in addition to the usual ones:\n'
+' - Are you hiding anything from me?\n'
+' - How do you really feel about me? '
,

' Whenever you Read a Person, you may choose from these questions in addition to the usual ones:\n'
+' - Are you hiding anything from me?\n'
+' - How do you really feel about me? '
,

' Whenever you Read a Person, you may choose from these questions in addition to the usual ones:\n'
+' - Are you hiding anything from me?\n'
+' - How do you really feel about me? '
]



,'accessthedarknet' : [
'# Access the Dark Net'
,

' You discover what you’re looking for, and may also choose one option:\n'
+' - You discover a portal to another dimension, and a path you can trace back to it later.\n'
+' - You make contact with someone – or something – who can help you, for the right price.\n'
+' - You find something valuable or important, in addition to what you were looking for. The GM will tell you what it is. '
,

' You find what you’re looking for, but you’re also exposed to repulsive and frightening stimuli. You must Keep it Together to see how it affects you. '
,

' You find what you’re after, but also contact something very dangerous. It might attempt to latch onto you or follow you back into reality. The GM makes a Move. '
]



,'bodyawareness' : [
'# Body Awareness'
,

' Choose one option. \nOptions:\n'
+' - Escape bindings or restraints.\n'
+' - Get past an obstacle (creature or object).\n'
+' - Get into or make it through a space you normally wouldn’t be able to. '
,

' Choose one option, but you expose yourself to danger or incur a cost. \nOptions:\n'
+' - Escape bindings or restraints.\n'
+' - Get past an obstacle (creature or object).\n'
+' - Get into or make it through a space you normally wouldn’t be able to. '
,

' Choose one option, but something goes very wrong. The GM makes a Move. \nOptions:\n'
+' - Escape bindings or restraints.\n'
+' - Get past an obstacle (creature or object).\n'
+' - Get into or make it through a space you normally wouldn’t be able to. '
]



,'daredevil' : [
'# Daredevil'
,

' Choose three Edges. You may spend them anytime during the scene. \nEdges:\n'
+' - Keep your eyes open: Discover a threat before it discovers you.\n'
+' - Get out of the way: Avoid an attack.\n'
+' - Get the jump on them: Harm your opponent before they can react '
,

' Choose two Edges. You may spend them anytime during the scene. \nEdges:\n'
+' - Keep your eyes open: Discover a threat before it discovers you.\n'
+' - Get out of the way: Avoid an attack.\n'
+' - Get the jump on them: Harm your opponent before they can react '
,

' Choose one Edge, but you are in over your head. The GM makes a Move. \nEdges:\n'
+' - Keep your eyes open: Discover a threat before it discovers you.\n'
+' - Get out of the way: Avoid an attack.\n'
+' - Get the jump on them: Harm your opponent before they can react. '
]



,'exitstrategy' : [
'# Exit Strategy'
,

' You get all three options below. \nOptions:\n'
+' - You leave the scene of the murder unnoticed and reach a safe spot of your choosing in the vicinity. Describe how.\n'
+' - You have left no clues that can be traced back to you.\n'
+' - The body is well hidden and will not be found for quite some time. '
,

' Choose two of the options below. \nOptions:\n'
+' - You leave the scene of the murder unnoticed and reach a safe spot of your choosing in the vicinity. Describe how.\n'
+' - You have left no clues that can be traced back to you.\n'
+' - The body is well hidden and will not be found for quite some time. '
,

' Choose one option, but you risk discovery or face unexpected obstacles. The GM makes a Move. \nOptions:\n'
+' - You leave the scene of the murder unnoticed and reach a safe spot of your choosing in the vicinity. Describe how.\n'
+' - You have left no clues that can be traced back to you.\n'
+' - The body is well hidden and will not be found for quite some time. '
]



,'eyefordetail' : [
'# Eye for Detail'
,

' Ask three questions from the list below. Questions:\n'
+' - Where are you from?\n'
+' - Are you capable of violence?\n'
+' - How could I seduce or tempt you?\n'
+' - Why are you here?\n'
+' - What are you working on? '
,

' Ask two questions from the list below. Questions:\n'
+' - Where are you from?\n'
+' - Are you capable of violence?\n'
+' - How could I seduce or tempt you?\n'
+' - Why are you here?\n'
+' - What are you working on? '
,

' Ask one question from the list below, but you expose your inquisitiveness to the person you’re observing. The GM makes a Move. Questions:\n'
+' - Where are you from?\n'
+' - Are you capable of violence?\n'
+' - How could I seduce or tempt you?\n'
+' - Why are you here?\n'
+' - What are you working on? '
]



,'hunter' : [
'# Hunter'
,

' Get three options. You may spend them anytime during this scene. \nOptions:\n'
+' - Set up an ambush for your enemy (deal your weapon’s Harm).\n'
+' - Camouflage (take +2 to Act Under Pressure while you are hiding).\n'
+' - Move in shadows (take +2 to Avoid Harm dealt with a ranged weapon). '
,

' Get two options. You may spend them anytime during this scene. \nOptions:\n'
+' - Set up an ambush for your enemy (deal your weapon’s Harm).\n'
+' - Camouflage (take +2 to Act Under Pressure while you are hiding).\n'
+' - Move in shadows (take +2 to Avoid Harm dealt with a ranged weapon). '
,

' Get one option, but you become the prey. The GM makes a Move. \nOptions:\n'
+' - Set up an ambush for your enemy (deal your weapon’s Harm).\n'
+' - Camouflage (take +2 to Act Under Pressure while you are hiding).\n'
+' - Move in shadows (take +2 to Avoid Harm dealt with a ranged weapon). '
]



,'instinct' : [
'# Instinct'
,

' Whenever you Observe a Situation and act on the GM’s answers, take +2 instead of +1. '
,

' Whenever you Observe a Situation and act on the GM’s answers, take +2 instead of +1. '
,

' Whenever you Observe a Situation and act on the GM’s answers, take +2 instead of +1. '
]



,'keen-eyed' : [
'# Keen-Eyed'
,

' Whenever you Observe a Situation, you may choose from these questions, in addition to the ones normally acquired:\n'
+' - What weaknesses do they have I can use to my advantage?\n'
+' - What strengths do they have I should watch out for? '
,

' Whenever you Observe a Situation, you may choose from these questions, in addition to the ones normally acquired:\n'
+' - What weaknesses do they have I can use to my advantage?\n'
+' - What strengths do they have I should watch out for? '
,

' Whenever you Observe a Situation, you may choose from these questions, in addition to the ones normally acquired:\n'
+' - What weaknesses do they have I can use to my advantage?\n'
+' - What strengths do they have I should watch out for? '
]



,'readacrowd' : [
'# Read a Crowd'
,

' Ask three questions. Questions:\n'
+' - Who here has information I want?\n'
+' - Where can I find what I am looking for?\n'
+' - Who is watching me?\n'
+' - Is there anything else of interest? '
,

' Ask two questions, but you also draw unwanted attention to yourself. Questions:\n'
+' - Who here has information I want?\n'
+' - Where can I find what I am looking for?\n'
+' - Who is watching me?\n'
+' - Is there anything else of interest? '
,

' Ask one question, but you’ve blown your cover. Those who have what you’re looking for will be expecting you. The GM makes a Move. Questions:\n'
+' - Who here has information I want?\n'
+' - Where can I find what I am looking for?\n'
+' - Who is watching me?\n'
+' - Is there anything else of interest? '
]



,'shadow' : [
'# Shadow'
,

' You avoid discovery, follow your target all the way to their final destination, and learn something about them you can use to your advantage later. \n\nAlternate Outcome:  You shake your pursuers and can choose to try to shadow them instead. '
,

' You avoid discovery and follow your target to their final destination. \n\nAlternate Outcome:   You shake your pursuers. '
,

' You are spotted or encounter some sort of problem along the way. The GM makes a Move. \n\nAlternate Outcome:  Your pursuers are still on your tail, and they can set up an ambush, disappear without a trace (only to show up when you least expect it), or refuse to go away. The GM makes a Move. '
]



,'survivalist' : [
'# Survivalist'
,

' Choose up to three options, useable while you remain in this situation. \nOptions:\n'
+' - Find water and something edible.\n'
+' - Make it past an environmental obstacle.\n'
+' - Find a safe spot to hide and rest. '
,

' Choose up to two options, useable while you remain in this situation. \nOptions:\n'
+' - Find water and something edible.\n'
+' - Make it past an environmental obstacle.\n'
+' - Find a safe spot to hide and rest. '
,

' Choose one option useable while you remain in this situation, but you’ve also overlooked something important. The GM makes a Move. \nOptions:\n'
+' - Find water and something edible.\n'
+' - Make it past an environmental obstacle.\n'
+' - Find a safe spot to hide and rest. '
]



,'wanderer' : [
'# Wanderer'
,

' You have been here before. Choose two options any time during your visit. \nOptions:\n'
+' - Ask the GM one question about this place.\n'
+' - You have a contact at this place who could help you, with a bit of convincing.\n'
+' - You have a hideout here, where you can put your head down and get some rest.\n'
+' - You know something about this place. Tell the others what. '
,

' You have heard of this place. Choose one option any time during your visit. \nOptions:\n'
+' - Ask the GM one question about this place.\n'
+' - You have a contact at this place who could help you, with a bit of convincing.\n'
+' - You have a hideout here, where you can put your head down and get some rest.\n'
+' - You know something about this place. Tell the others what. '
,

' You have been here before, but something bad happened. Choose one option any time during your visit. The GM explains what kind of problem awaits you here and makes a Move. \nOptions:\n'
+' - Ask the GM one question about this place.\n'
+' - You have a contact at this place who could help you, with a bit of convincing.\n'
+' - You have a hideout here, where you can put your head down and get some rest.\n'
+' - You know something about this place. Tell the others what. '
]



,'analyst' : [
'# Analyst'
,

' Whenever you Investigate something, you may also choose from these additional questions:\n'
+' - Which organizations, groups, or people of interest may be connected to this?\n'
+' - Is there a connection between this and another event?\n'
+' - What could a plausible motive be? '
,

' Whenever you Investigate something, you may also choose from these additional questions:\n'
+' - Which organizations, groups, or people of interest may be connected to this?\n'
+' - Is there a connection between this and another event?\n'
+' - What could a plausible motive be? '
,

' Whenever you Investigate something, you may also choose from these additional questions:\n'
+' - Which organizations, groups, or people of interest may be connected to this?\n'
+' - Is there a connection between this and another event?\n'
+' - What could a plausible motive be? '
]



,'battlefieldmedicine' : [
'# Battlefield Medicine'
,

' Choose two options. \nOptions:\n'
+' - Improvisation: You stabilize one Wound without access to medical equipment.\n'
+' - Efective: You stabilize two Wounds instead of one.\n'
+' - Careful: The wound stabilizes and will heal much faster than normal. '
,

' You may choose one option. \nOptions:\n'
+' - Improvisation: You stabilize one Wound without access to medical equipment.\n'
+' - Efective: You stabilize two Wounds instead of one.\n'
+' - Careful: The wound stabilizes and will heal much faster than normal. \n\nHowever, you must also choose one complication:\n'
+' - You leave cosmetic scars or defects (the patient loses Stability (−2).\n'
+' - There are lingering side effects (−1 to all rolls the wound could feasibly affect until it’s fully healed).\n'
+' - The patient remains knocked out until the GM determines that they awaken. '
,

' You stabilize the wound, even without access to medical equipment, but there are also unexpected and potentially dangerous consequences, such as infections, healing deformities, or other serious side effects. The GM makes a Move. '
]



,'collector' : [
'# Collector'
,

' You know exactly where the item is, how to acquire it, and how to minimize hazards, obstacles, and/or costs. '
,

' You know roughly where it is and what hazards, obstacles, and/or costs are associated with acquiring it. '
,

' You know roughly where to start searching for it, but not the hazards or costs involved in pursuing it. '
]



,'crimesceneinvestigator' : [
'# Crime Scene Investigator'
,

' Ask two questions. Questions:\n'
+' - What was the chain of events?\n'
+' - What can I assume about the perpetrator?\n'
+' - Which mistakes did the perpetrator make?\n'
+' - When was the crime committed?\n'
+' - When was someone here last?\n'
+' - Does the crime remind me of something I am familiar with already and, if so, what?\n'
+' - Who might know more about the crime? '
,

' Ask one question. Questions:\n'
+' - What was the chain of events?\n'
+' - What can I assume about the perpetrator?\n'
+' - Which mistakes did the perpetrator make?\n'
+' - When was the crime committed?\n'
+' - When was someone here last?\n'
+' - Does the crime remind me of something I am familiar with already and, if so, what?\n'
+' - Who might know more about the crime? '
,

' Ask one question, but your investigation leads you into danger or introduces additional problems later on. Questions:\n'
+' - What was the chain of events?\n'
+' - What can I assume about the perpetrator?\n'
+' - Which mistakes did the perpetrator make?\n'
+' - When was the crime committed?\n'
+' - When was someone here last?\n'
+' - Does the crime remind me of something I am familiar with already and, if so, what?\n'
+' - Who might know more about the crime? '
]



,'dataretrieval' : [
'# Data Retrieval'
,

' Ask three questions. Questions:\n'
+' - What is its origin?\n'
+' - What is it meant for?\n'
+' - How does it work?\n'
+' - What do I have to watch out for?\n'
+' - How can I stop or destroy this? '
,

' Ask two questions. Questions:\n'
+' - What is its origin?\n'
+' - What is it meant for?\n'
+' - How does it work?\n'
+' - What do I have to watch out for?\n'
+' - How can I stop or destroy this? '
,

' Ask one question, but you also discover something unexpected. The GM makes a Move. Questions:\n'
+' - What is its origin?\n'
+' - What is it meant for?\n'
+' - How does it work?\n'
+' - What do I have to watch out for?\n'
+' - How can I stop or destroy this? '
]



,'expert' : [
'# Expert'
,

' You are an expert in certain fields of knowledge. Whenever you Investigate something associated with one of your chosen fields, you always get to ask one additional question, regardless of the outcome, and may ask any questions you want: Choose two areas of expertise:\n'
+' - Archeology\n'
+' - Economics\n'
+' - History\n'
+' - Comparative literature\n'
+' - Psychology\n'
+' - Sociology\n'
+' - Theology\n'
+' - (Other) '
,

' You are an expert in certain fields of knowledge. Whenever you Investigate something associated with one of your chosen fields, you always get to ask one additional question, regardless of the outcome, and may ask any questions you want: Choose two areas of expertise:\n'
+' - Archeology\n'
+' - Economics\n'
+' - History\n'
+' - Comparative literature\n'
+' - Psychology\n'
+' - Sociology\n'
+' - Theology\n'
+' - (Other) '
,

' You are an expert in certain fields of knowledge. Whenever you Investigate something associated with one of your chosen fields, you always get to ask one additional question, regardless of the outcome, and may ask any questions you want: Choose two areas of expertise:\n'
+' - Archeology\n'
+' - Economics\n'
+' - History\n'
+' - Comparative literature\n'
+' - Psychology\n'
+' - Sociology\n'
+' - Theology\n'
+' - (Other) '
]



,'explosivesexpert' : [
'# Explosives Expert'
,

' You construct a functional bomb (see Explosives in Chapter 4 – The Player Character). \n\nAlternate Outcome:  The bomb is deactivated. '
,

' The bomb’s blast potential is lower than usual (decrease Harm dealt by −1). \n\nAlternate Outcome:  Complications arise. Maybe you can’t completely turn it off, just delay the timer, weaken the explosive effect, or something else turns up and makes thing worse. '
,

' The bomb is unpredictable. Maybe it doesn’t detonate, detonates prematurely, or it is more powerful and volatile than expected. The GM makes a Move. \n\nAlternate Outcome:  Fuck, that’s not good! The bomb may go off in your hands, the timer starts counting down from 10, 9, 8, 7..., or even bigger problems occur. The GM makes a Move. '
]



,'hacker' : [
'# Hacker'
,

' You accomplish your task without a problem. '
,

' Complications arise. Choose one option:\n'
+' - Someone discovers the intrusion. You must take risks or compromise on how much you’re able to accomplish.\n'
+' - You leave traces of your intrusion. '
,

' Unbeknownst to you, your intrusion didn’t work out as you wanted. Maybe you didn’t succeed at your task as well as you imagined, or you may have been discovered by personal enemies, law enforcement, or something else lurking in the network. The GM makes a Move. '
]



,'inventor' : [
'# Inventor'
,

' The construction is successful and you may pick two options from below. \nOptions:\n'
+' - Durable: The construction can be used multiple times and doesn’t break easily.\n'
+' - Effective: The construction confers +1 on rolls where it is used for its intended purpose.\n'
+' - Lethal: The construction causes +1 Harm.\n'
+' - Protective: The construction confers +1 armor. '
,

' The construction has minor flaws. You may choose one option from below. \nOptions:\n'
+' - Durable: The construction can be used multiple times and doesn’t break easily.\n'
+' - Effective: The construction confers +1 on rolls where it is used for its intended purpose.\n'
+' - Lethal: The construction causes +1 Harm.\n'
+' - Protective: The construction confers +1 armor. '
,

' You complete the construction or repair, but it has significant flaws, some of which are hidden. The GM makes a Move. '
]



,'manhunter' : [
'# Manhunter'
,

' Ask the GM three questions from the list below. Questions:\n'
+' - What is their background?\n'
+' - What or who do they love most of all?\n'
+' - Who do they surround themselves with, like, and/or trust?\n'
+' - Where are they located right now?\n'
+' - How can I best gain access to them? '
,

' Ask the GM two questions from the list below. Questions:\n'
+' - What is their background?\n'
+' - What or who do they love most of all?\n'
+' - Who do they surround themselves with, like, and/or trust?\n'
+' - Where are they located right now?\n'
+' - How can I best gain access to them? '
,

' Ask the GM one question from the list below, but someone figures out you’ve been snooping around. Questions:\n'
+' - What is their background?\n'
+' - What or who do they love most of all?\n'
+' - Who do they surround themselves with, like, and/or trust?\n'
+' - Where are they located right now?\n'
+' - How can I best gain access to them? '
]



,'occultlibrary' : [
'# Occult Library'
,

' Ask the GM two questions from the list below. Questions:\n'
+' - Which higher power does this have connections to?\n'
+' - What do I need, or need to do, to exorcise or control this being?\n'
+' - Which dimension is this associated with?\n'
+' - What must I do to protect myself from this? '
,

' Ask the GM one question from the list below. Questions:\n'
+' - Which higher power does this have connections to?\n'
+' - What do I need, or need to do, to exorcise or control this being?\n'
+' - Which dimension is this associated with?\n'
+' - What must I do to protect myself from this? '
,

' Ask the GM one question from the list below, but you have missed or overlooked something crucial. The GM takes 1 Hold, which can be spent at any time to make a hard or soft Move. Questions:\n'
+' - Which higher power does this have connections to?\n'
+' - What do I need, or need to do, to exorcise or control this being?\n'
+' - Which dimension is this associated with?\n'
+' - What must I do to protect myself from this? '
]



,'occultstudies' : [
'# Occult Studies'
,

' Take both options below. \nOptions:\n'
+' - I know something about this (ask the GM what you know and take +1 ongoing while acting on the answers during this scene).\n'
+' - I know where I can find more information about this (ask the GM where). '
,

' Choose one option. \nOptions:\n'
+' - I know something about this (ask the GM what you know and take +1 ongoing while acting on the answers during this scene).\n'
+' - I know where I can find more information about this (ask the GM where). '
,

' You have a hazy memory of something like this, but can’t say for sure if it’s true or not. The GM explains what it is you remember. '
]



,'prepared' : [
'# Prepared'
,

' Choose three options. \nOptions:\n'
+' - Find or create a map of the location.\n'
+' - Uncover any security systems and other obstacles.\n'
+' - Pinpoint the location of something you’re after. '
,

' Choose two options. \nOptions:\n'
+' - Find or create a map of the location.\n'
+' - Uncover any security systems and other obstacles.\n'
+' - Pinpoint the location of something you’re after. '
,

' Choose one option, but you have missed or overlooked something crucial. The GM takes 1 Hold, which can be spent at any time to make a hard or soft Move for the location. \nOptions:\n'
+' - Find or create a map of the location.\n'
+' - Uncover any security systems and other obstacles.\n'
+' - Pinpoint the location of something you’re after. '
]



,'puppeteer' : [
'# Puppeteer'
,

' Everyone involved takes +1 ongoing to carry out the plan, and you get one Experience if the plan is successful. '
,

' You get one Experience if the plan is successful, but you have overlooked or miscalculated something. '
,

' Your plan is inadequate, revealed, and/or misguided. The GM makes a Move. '
]



,'quickthinker' : [
'# Quick Thinker'
,

' Choose up to three options, at any time during the mission. \nOptions:\n'
+' - Remember something that’s advantageous in a negotiation. Ask the GM what it is.\n'
+' - You possess some equipment you can use to get out of a sticky situation. Ask the GM what it is.\n'
+' - You have special field training that would be useful in getting past one of your obstacles. Ask the GM what it is. '
,

' Choose up to two options, at any time during the mission. \nOptions:\n'
+' - Remember something that’s advantageous in a negotiation. Ask the GM what it is.\n'
+' - You possess some equipment you can use to get out of a sticky situation. Ask the GM what it is.\n'
+' - You have special field training that would be useful in getting past one of your obstacles. Ask the GM what it is. '
,

' At any time during the mission, choose one option, but you’ve failed to account for something. The GM makes a Move. \nOptions:\n'
+' - Remember something that’s advantageous in a negotiation. Ask the GM what it is.\n'
+' - You possess some equipment you can use to get out of a sticky situation. Ask the GM what it is.\n'
+' - You have special field training that would be useful in getting past one of your obstacles. Ask the GM what it is. '
]



,'scientist' : [
'# Scientist'
,

' Whenever you Investigate an object or entity using the proper equipment, you may choose from these following questions, in addition to those acquired through investigation: Questions:\n'
+' - What properties does this have? (take +1 to any rolls against entities or objects of a similar type next time you encounter it).\n'
+' - How do I make use of this? (take +1 to any rolls associated with using the object).\n'
+' - What is its purpose? '
,

' Whenever you Investigate an object or entity using the proper equipment, you may choose from these following questions, in addition to those acquired through investigation: Questions:\n'
+' - What properties does this have? (take +1 to any rolls against entities or objects of a similar type next time you encounter it).\n'
+' - How do I make use of this? (take +1 to any rolls associated with using the object).\n'
+' - What is its purpose? '
,

' Whenever you Investigate an object or entity using the proper equipment, you may choose from these following questions, in addition to those acquired through investigation: Questions:\n'
+' - What properties does this have? (take +1 to any rolls against entities or objects of a similar type next time you encounter it).\n'
+' - How do I make use of this? (take +1 to any rolls associated with using the object).\n'
+' - What is its purpose? '
]



,'tracer' : [
'# Tracer'
,

' Ask up to three of the questions below. Questions:\n'
+' - Where in the world was this seen last?\n'
+' - What people have associated themselves with what I’m looking for lately?\n'
+' - What tracks and marks has it left behind?\n'
+' - Who else is trying to find what I’m looking for? '
,

' Ask up to two of the questions below. Questions:\n'
+' - Where in the world was this seen last?\n'
+' - What people have associated themselves with what I’m looking for lately?\n'
+' - What tracks and marks has it left behind?\n'
+' - Who else is trying to find what I’m looking for? '
,

' Ask one of the questions, but someone notices you snooping around. It might be someone you’d rather not be known by, or a traitor inside your network. Questions:\n'
+' - Where in the world was this seen last?\n'
+' - What people have associated themselves with what I’m looking for lately?\n'
+' - What tracks and marks has it left behind?\n'
+' - Who else is trying to find what I’m looking for? '
]



,'artifact' : [
'# Artifact'
,

' Choose one option (the GM determines what happens). The GM may wish to modify this list of options, either on their own or by working together with the player to come up with what exactly the PC’s artifact can do.\n'
+' - See the true form of a creature or location.\n'
+' - Receive a vision of what threatens you.\n'
+' - Get yourself out of a bind.\n'
+' - Call on the entity bound to the artifact and bargain with them. '
,

' Choose one option (the GM determines what happens). However, the artifact also exacts an additional price (the GM determines what is required). The GM may wish to modify this list of options, either on their own or by working together with the player to come up with what exactly the PC’s artifact can do.\n'
+' - See the true form of a creature or location.\n'
+' - Receive a vision of what threatens you.\n'
+' - Get yourself out of a bind.\n'
+' - Call on the entity bound to the artifact and bargain with them. '
,

' The artifact does something unexpected, possibly dangerous. The GM makes a Move. '
]



,'bound' : [
'# Bound'
,

' You may choose up to three options at any time during the session. \nOptions:\n'
+' - See the true form of a creature or location.\n'
+' - Disperse magic targeting you.\n'
+' - Call on the entity. '
,

' You may choose one option at any time during the session. \nOptions:\n'
+' - See the true form of a creature or location.\n'
+' - Disperse magic targeting you.\n'
+' - Call on the entity. '
,

' You may choose one option at any time during the session, but the GM makes a Move for the entity at some point during the session. \nOptions:\n'
+' - See the true form of a creature or location.\n'
+' - Disperse magic targeting you.\n'
+' - Call on the entity. '
]



,'charismaticaura' : [
'# Charismatic Aura'
,

' Choose two separate options. \nOptions:\n'
+' - Catch a stranger’s attention. They become curious and approach you.\n'
+' - Change a person’s disposition towards you from either aggressive to suspicious, suspicious to neutral, or neutral to positive.\n'
+' - Make opponents perceive you as harmless and ignore you for as long as you remain in the background and do not act against them. '
,

' Choose one option. \nOptions:\n'
+' - Catch a stranger’s attention. They become curious and approach you.\n'
+' - Change a person’s disposition towards you from either aggressive to suspicious, suspicious to neutral, or neutral to positive.\n'
+' - Make opponents perceive you as harmless and ignore you for as long as you remain in the background and do not act against them. '
,

' Choose one option, but you also attract unwanted attention. The GM makes a Move. \nOptions:\n'
+' - Catch a stranger’s attention. They become curious and approach you.\n'
+' - Change a person’s disposition towards you from either aggressive to suspicious, suspicious to neutral, or neutral to positive.\n'
+' - Make opponents perceive you as harmless and ignore you for as long as you remain in the background and do not act against them. '
]



,'contagiousinsanity' : [
'# Contagious Insanity'
,

' Choose two options. \nOptions:\n'
+' - Afflict your victim with a temporary psychosis, in which they are haunted by their fears (NPCs only).\n'
+' - Trigger a Disadvantage within another person (PCs only, roll for the Disadvantage).\n'
+' - Affect an additional victim.\n'
+' - Call for creatures of madness to haunt the infected. '
,

' Choose one option. \nOptions:\n'
+' - Afflict your victim with a temporary psychosis, in which they are haunted by their fears (NPCs only).\n'
+' - Trigger a Disadvantage within another person (PCs only, roll for the Disadvantage).\n'
+' - Affect an additional victim.\n'
+' - Call for creatures of madness to haunt the infected. '
,

' Your intended victim’s own terrors and Dark Secrets manifest within you, instead. You must Keep it Together. '
]



,'cultleader' : [
'# Cult Leader'
,

' Choose to receive up to three visions from the list below. Visions:\n'
+' - A creature’s true form.\n'
+' - A portal between dimensions.\n'
+' - The cult’s enemies.\n'
+' - The purpose of an object.\n'
+' - Your deity’s wishes (take +1 to all rolls while fulfilling their wishes). '
,

' Choose to receive up to two visions from the list below. Visions:\n'
+' - A creature’s true form.\n'
+' - A portal between dimensions.\n'
+' - The cult’s enemies.\n'
+' - The purpose of an object.\n'
+' - Your deity’s wishes (take +1 to all rolls while fulfilling their wishes). '
,

' Choose one vision, but the Illusion tears as a result. You may temporarily be transported into another dimension, attract a demonic being’s attention, or receive a horrifying omen. The GM makes a Move. Visions:\n'
+' - A creature’s true form.\n'
+' - A portal between dimensions.\n'
+' - The cult’s enemies.\n'
+' - The purpose of an object.\n'
+' - Your deity’s wishes (take +1 to all rolls while fulfilling their wishes). '
]



,'dabblerintheoccult' : [
'# Dabbler in the Occult'
,

' You perform every step correctly; the ritual works as intended. '
,

' You make a minor error. The GM chooses one complication:\n'
+' - You do not have working protection against the forces or entities the ritual summons.\n'
+' - The effects of the ritual are slightly different than what you had imagined.\n'
+' - The ritual summons unexpected entities or forces. '
,

' You misunderstand the scripture and perform the ritual with no control whatsoever over the resulting outcome. The GM makes a Move. '
]



,'divine' : [
'# Divine'
,

' The creature mistakes you for a god. Choose up to three options, useable any time during this scene. \nOptions:\n'
+' - Soothe an aggressive creature.\n'
+' - Command the creature and force it to obey your order. '
,

' You are fascinating to the creature. Choose one option. \nOptions:\n'
+' - Soothe an aggressive creature.\n'
+' - Command the creature and force it to obey your order. '
,

' You may choose one option, but after using it the creature becomes determined to possess you. It might try to devour you or perhaps capture you. The GM makes a Move. \nOptions:\n'
+' - Soothe an aggressive creature.\n'
+' - Command the creature and force it to obey your order. '
]



,'dreamer' : [
'# Dreamer'
,

' You meet the intended person or arrive at the specific place in the Dream. '
,

' You meet the intended person, or arrive at the specific place. However, some element has changed, or something followed you or the person in question. '
,

' You are lost in the Dream and cannot wake up until you find your way back. '
]



,'enhancedawareness' : [
'# Enhanced Awareness'
,

' You can discern clear details regarding the location. '
,

' You get some basic impressions regarding the location. '
,

' The Illusion tears. The veil is lifted temporarily, revealing an alternate dimension – the GM determines which one. The PC could be sucked into it or something may cross over into our reality. The GM makes a Move. '
]



,'exorcist' : [
'# Exorcist'
,

' The creature is banished. Choose two options. \nOptions:\n'
+' - Nobody is harmed during the ritual.\n'
+' - The entity will not reappear later.\n'
+' - The entity will not become hostile toward you. '
,

' The creature is banished. Choose one option. \nOptions:\n'
+' - Nobody is harmed during the ritual.\n'
+' - The entity will not reappear later.\n'
+' - The entity will not become hostile toward you. '
,

' The creature resists banishment and something goes terribly wrong, such as the creature possessing you. The GM makes a Move. '
]



,'forbiddeninspiration' : [
'# Forbidden Inspiration'
,

' Choose two options. \nOptions:\n'
+' - Enticement: Entice an entity to come to you.\n'
+' - Visions: See Through the Illusion into a specific place of your choice.\n'
+' - Inspiration: Ask the GM if there is anything strange or supernatural about the situation you’re in. The answer will be revealed through your art. '
,

' Choose one option. \nOptions:\n'
+' - Enticement: Entice an entity to come to you.\n'
+' - Visions: See Through the Illusion into a specific place of your choice.\n'
+' - Inspiration: Ask the GM if there is anything strange or supernatural about the situation you’re in. The answer will be revealed through your art. '
,

' You have gazed too deeply into the abyss. Choose one option, but you also experience terrifying visions or encounter something horrible. The GM makes a Move. \nOptions:\n'
+' - Enticement: Entice an entity to come to you.\n'
+' - Visions: See Through the Illusion into a specific place of your choice.\n'
+' - Inspiration: Ask the GM if there is anything strange or supernatural about the situation you’re in. The answer will be revealed through your art. '
]



,'genius' : [
'# Genius'
,

' Choose up to three Edges, useable any time in the scene, while you’re still in danger. \nEdges:\n'
+' - Logical: You realize an effective way to dispose of the threat. Deal +1 Harm whenever you exploit it.\n'
+' - Quick thinker: You realize how to protect yourself from Harm. Treat it as if you’d rolled a 15+ on Avoid Harm whenever you exploit it.\n'
+' - Rational: You realize how to save yourself by sacrificing someone else. Pick the person you utilize to escape the threat. '
,

' Choose up to two Edges, useable any time in the scene, while you’re still in danger. \nEdges:\n'
+' - Logical: You realize an effective way to dispose of the threat. Deal +1 Harm whenever you exploit it.\n'
+' - Quick thinker: You realize how to protect yourself from Harm. Treat it as if you’d rolled a 15+ on Avoid Harm whenever you exploit it.\n'
+' - Rational: You realize how to save yourself by sacrificing someone else. Pick the person you utilize to escape the threat. '
,

' Choose one Edge, but you also attract unwanted attention. The GM makes a Move. \nEdges:\n'
+' - Logical: You realize an effective way to dispose of the threat. Deal +1 Harm whenever you exploit it.\n'
+' - Quick thinker: You realize how to protect yourself from Harm. Treat it as if you’d rolled a 15+ on Avoid Harm whenever you exploit it.\n'
+' - Rational: You realize how to save yourself by sacrificing someone else. Pick the person you utilize to escape the threat. '
]



,'implantedmessages' : [
'# Implanted Messages'
,

' You hold 2 Power over them. For as long as you retain Power over them, they take 1 Serious Wound should they refuse or attempt to go against your order, but this loosens your grip over them by 1 Power. If they fulfill your order, all your remaining Power over them is removed. '
,

' You hold 1 Power over them. For as long as you retain Power over them, they take 1 Serious Wound should they refuse or attempt to go against your order, but this loosens your grip over them by 1 Power. If they fulfill your order, all your remaining Power over them is removed. '
,

' Something goes wrong, such as they get hurt in the process or the order’s outcome is different than what you imagined. The GM makes a Move. '
]



,'innerpower' : [
'# Inner Power'
,

' The power attacks all opponents in your vicinity, causing 2 Harm. '
,

' The power attacks your closest opponent, causing 2 Harm. '
,

' The power attacks all living beings, including yourself, in the vicinity, causing 2 Harm. '
]



,'layonhands' : [
'# Lay on Hands'
,

' You fully heal the injured person, channeling the Wound onto yourself or a selected target. '
,

' You stabilize the injured, channeling the Wound onto yourself or a selected target. '
,

' You may choose to stabilize the injured, but if you do, the powers break free from your control. '
]



,'magicalintuition' : [
'# Magical Intuition'
,

' Choose up to three options. Up to two may be saved until later this scene. \nOptions:\n'
+' - Learn something about a creature’s true nature.\n'
+' - Learn if something has a magical nature.\n'
+' - Learn where the Illusion is weakest towards other dimensions. '
,

' Choose up to two options. One may be saved until later this scene. \nOptions:\n'
+' - Learn something about a creature’s true nature.\n'
+' - Learn if something has a magical nature.\n'
+' - Learn where the Illusion is weakest towards other dimensions. '
,

' Choose one option, but you also get an unexpected vision or attract attention. The GM makes a Move. \nOptions:\n'
+' - Learn something about a creature’s true nature.\n'
+' - Learn if something has a magical nature.\n'
+' - Learn where the Illusion is weakest towards other dimensions. '
]



,'magneticattraction' : [
'# Magnetic Attraction'
,

' Choose up to three options. You may save up to two until later in the scene. \nOptions:\n'
+' - People forget what they’re doing and can do nothing but stare at you.\n'
+' - Draw someone to you.\n'
+' - Get someone to do what you ask. '
,

' Choose one option. \nOptions:\n'
+' - People forget what they’re doing and can do nothing but stare at you.\n'
+' - Draw someone to you.\n'
+' - Get someone to do what you ask. '
,

' Choose one option, but someone present becomes obsessed, wanting to have you, keep you, and own you for themselves. The GM makes a Move. \nOptions:\n'
+' - People forget what they’re doing and can do nothing but stare at you.\n'
+' - Draw someone to you.\n'
+' - Get someone to do what you ask. '
]



,'sixthsense' : [
'# Sixth Sense'
,

' Choose up to three options, useable any time during the session. \nOptions:\n'
+' - Act first in a threatening situation. This can include even acting prior to a surprise attack.\n'
+' - Sense whether someone wishes good or ill towards you.\n'
+' - Discover or sense a clue or lead when you’re off track. '
,

' Choose up to two options, useable any time during the session. \nOptions:\n'
+' - Act first in a threatening situation. This can include even acting prior to a surprise attack.\n'
+' - Sense whether someone wishes good or ill towards you.\n'
+' - Discover or sense a clue or lead when you’re off track. '
,

' Your instincts will fail to trigger in a dangerous situation. The GM makes a Move at some point during the session. '
]



,'snakecharmer' : [
'# Snake Charmer'
,

' Choose one option immediately, and you may choose up to two more any time in the future. \nOptions:\n'
+' - Ask the creature for help with a problem.\n'
+' - Ask the creature for something you desire. '
,

' Choose one option. \nOptions:\n'
+' - Ask the creature for help with a problem.\n'
+' - Ask the creature for something you desire. '
,

' The desire is beyond the creature’s ability to regulate. It cannot help but attempt to devour or imprison you. '
]



,'stubborn' : [
'# Stubborn'
,

' Get 3 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Refuse to give up: Postpone the effects of a critical injury until you have made it out of the threat’s reach.\n'
+' - Will over skill: Roll +Willpower instead of the normal attribute whenever you avoid or fight whatever is threatening you.\n'
+' - Steel yourself: Break free from a supernatural effect. '
,

' Get 2 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Refuse to give up: Postpone the effects of a critical injury until you have made it out of the threat’s reach.\n'
+' - Will over skill: Roll +Willpower instead of the normal attribute whenever you avoid or fight whatever is threatening you.\n'
+' - Steel yourself: Break free from a supernatural effect. '
,

' Get 1 Edge, but you push yourself past your breaking point. Decrease Stability (−2). \nEdges:\n'
+' - Refuse to give up: Postpone the effects of a critical injury until you have made it out of the threat’s reach.\n'
+' - Will over skill: Roll +Willpower instead of the normal attribute whenever you avoid or fight whatever is threatening you.\n'
+' - Steel yourself: Break free from a supernatural effect. '
]



,'voiceofinsanity' : [
'# Voice of Insanity'
,

' Choose up to three options, useable any time during this scene. \nOptions:\n'
+' - Attract other people to join in the crowd.\n'
+' - Have crowd members give you all their valuables.\n'
+' - Unite the crowd to fight for you.\n'
+' - Incite the crowd into an orgy of unbridled emotion: sexual lust, anger, sorrow, violence, generosity, or celebrating, depending on what concepts you are instilling into them.\n'
+' - Have the crowd disperse and calmly return to their normal lives. '
,

' Choose up to two options, useable any time during this scene. \nOptions:\n'
+' - Attract other people to join in the crowd.\n'
+' - Have crowd members give you all their valuables.\n'
+' - Unite the crowd to fight for you.\n'
+' - Incite the crowd into an orgy of unbridled emotion: sexual lust, anger, sorrow, violence, generosity, or celebrating, depending on what concepts you are instilling into them.\n'
+' - Have the crowd disperse and calmly return to their normal lives. '
,

' Choose one option, useable any time during this scene. However, the crowd becomes uncontrollable and volatile, and cannot be dispersed. The GM makes a Move. \nOptions:\n'
+' - Attract other people to join in the crowd.\n'
+' - Have crowd members give you all their valuables.\n'
+' - Unite the crowd to fight for you.\n'
+' - Incite the crowd into an orgy of unbridled emotion: sexual lust, anger, sorrow, violence, generosity, or celebrating, depending on what concepts you are instilling into them.\n'
+' - Have the crowd disperse and calmly return to their normal lives. '
]



,'voiceofpain' : [
'# Voice of Pain'
,

' You get two options. \nOptions:\n'
+' - You realize how to get through your opponent’s defenses (take +1 to Engage in Combat with them).\n'
+' - You find your opponent’s weak spot (deal +1 Harm whenever you Engage in Combat with them).\n'
+' - You perceive your opponent’s pattern of attack (take +1 to Avoid Harm whenever they attack you). These effects are permanent against this opponent. '
,

' Choose one option. \nOptions:\n'
+' - You realize how to get through your opponent’s defenses (take +1 to Engage in Combat with them).\n'
+' - You find your opponent’s weak spot (deal +1 Harm whenever you Engage in Combat with them).\n'
+' - You perceive your opponent’s pattern of attack (take +1 to Avoid Harm whenever they attack you). These effects are permanent against this opponent. '
,

' Choose one option, but the pain will overwhelm you eventually and make you black out. \nOptions:\n'
+' - You realize how to get through your opponent’s defenses (take +1 to Engage in Combat with them).\n'
+' - You find your opponent’s weak spot (deal +1 Harm whenever you Engage in Combat with them).\n'
+' - You perceive your opponent’s pattern of attack (take +1 to Avoid Harm whenever they attack you). These effects are permanent against this opponent. '
]



,'wayfinder' : [
'# Wayfinder'
,

' You discover a shortcut through the alleys, which takes you to your destination within a few minutes, regardless of how far the distance actually is. '
,

' You discover a shortcut, but there is also some sort of obstacle you will need to get past. '
,

' You discover a shortcut, but it leads you into a dangerous situation, such as the lair of some creature or an ambush set by some gang. The GM makes a Move. '
]



,'deadlystare' : [
'# Deadly Stare'
,

' You make eye contact with an NPC, causing them to freeze up and be unable to take any actions until you break eye contact. You also get +2 ongoing against your target. '
,

' You make eye contact with an NPC, causing them to freeze up and be unable to take any actions until you break eye contact. '
,

' Your opponents see you as their primary threat. '
]



,'deathdrive' : [
'# Death Drive'
,

' Get 3 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Eager: Engage an additional hostile in Combat.\n'
+' - Vicious: deal +2 Harm with one attack.\n'
+' - Frantic: get within reach to attack a hostile.\n'
+' - Reckless: frighten your opponents by laughing into the face of death (+1 ongoing during the fight). '
,

' Get 2 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Eager: Engage an additional hostile in Combat.\n'
+' - Vicious: deal +2 Harm with one attack.\n'
+' - Frantic: get within reach to attack a hostile.\n'
+' - Reckless: frighten your opponents by laughing into the face of death (+1 ongoing during the fight). '
,

' Get 1 Edge, but afterwards you discover you have been injured without noticing it (Endure Injury; the GM determines the amount of Harm based on who attacked you and how). \nEdges:\n'
+' - Eager: Engage an additional hostile in Combat.\n'
+' - Vicious: deal +2 Harm with one attack.\n'
+' - Frantic: get within reach to attack a hostile.\n'
+' - Reckless: frighten your opponents by laughing into the face of death (+1 ongoing during the fight). '
]



,'enforcer' : [
'# Enforcer'
,

' They must decide to either do what you want or defy you with the knowledge that you can execute your threat. '
,

' You must give them a third option. Choose one:\n'
+' - They offer you something they think you’d rather have.\n'
+' - Retreat from the scene.\n'
+' - They are terrorized; you have +1 ongoing on all rolls against them until they’ve proven they’re not afraid of you.\n'
+' - They attack you from a disadvantaged position. You take +2 on your roll to Engage in Combat if you counterattack. '
,

' Turns out you didn’t have the advantage you thought you did. The GM makes a Move. '
]



,'fieldagent' : [
'# Field Agent'
,

' Get 3 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Take cover: avoid a ranged attack by diving behind an object or a person.\n'
+' - Choke hold: lock a human opponent in a grip they cannot get out of without taking 1 Harm.\n'
+' - Disarm: remove an opponent’s weapon in close combat.\n'
+' - Improvised weapon: execute a lethal, close-combat attack with a seemingly innocuous object (Surprise Strike [2], [Distance: arm]). '
,

' Get 2 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Take cover: avoid a ranged attack by diving behind an object or a person.\n'
+' - Choke hold: lock a human opponent in a grip they cannot get out of without taking 1 Harm.\n'
+' - Disarm: remove an opponent’s weapon in close combat.\n'
+' - Improvised weapon: execute a lethal, close-combat attack with a seemingly innocuous object (Surprise Strike [2], [Distance: arm]). '
,

' Get 1 Edge, but you have made a bad call. The GM makes a Move. \nEdges:\n'
+' - Take cover: avoid a ranged attack by diving behind an object or a person.\n'
+' - Choke hold: lock a human opponent in a grip they cannot get out of without taking 1 Harm.\n'
+' - Disarm: remove an opponent’s weapon in close combat.\n'
+' - Improvised weapon: execute a lethal, close-combat attack with a seemingly innocuous object (Surprise Strike [2], [Distance: arm]). '
]



,'gangleader' : [
'# Gang Leader'
,

' They enact your orders without question. '
,

' They do as you want, but there is a complication (choose one):\n'
+' - One of them defies you in front of the others.\n'
+' - They will all be disgruntled for some time. '
,

' Problems arise. Maybe something goes wrong when carrying out your orders, or they doubt your abilities as a leader. The GM makes a Move. '
]



,'intimidating' : [
'# Intimidating'
,

' They succumb to fear and give in to your demands. '
,

' They run away from you or give in to you, GM’s choice. '
,

' They see you as their primary threat and act accordingly. The GM makes a Move for them. '
]



,'lightningfast' : [
'# Lightning Fast'
,

' Get 3 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Dodge: avoid an attack.\n'
+' - Blinding speed: Engage in Combat with every opponent within reach of your weapon as a single attack. If you’re attacking with a firearm, this uses up all its ammo.\n'
+' - Uncanny precision: hit your opponent’s weak spot. Deal +1 Harm. '
,

' Get 2 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Dodge: avoid an attack.\n'
+' - Blinding speed: Engage in Combat with every opponent within reach of your weapon as a single attack. If you’re attacking with a firearm, this uses up all its ammo.\n'
+' - Uncanny precision: hit your opponent’s weak spot. Deal +1 Harm. '
,

' Get 1 Edge, but you also end up in a bad spot or face unexpected resistance. The GM makes a Move. \nEdges:\n'
+' - Dodge: avoid an attack.\n'
+' - Blinding speed: Engage in Combat with every opponent within reach of your weapon as a single attack. If you’re attacking with a firearm, this uses up all its ammo.\n'
+' - Uncanny precision: hit your opponent’s weak spot. Deal +1 Harm. '
]



,'martialartsexpert' : [
'# Martial Arts Expert'
,

' Get 2 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Block: avoid a melee attack.\n'
+' - Roundhouse strike: Engage in Combat against several opponents surrounding you, counting as a single attack.\n'
+' - Disarm: remove an opponent’s weapon.\n'
+' - Throw: reposition an opponent or drop them to the ground. '
,

' Get 1 Edge. \nEdges:\n'
+' - Block: avoid a melee attack.\n'
+' - Roundhouse strike: Engage in Combat against several opponents surrounding you, counting as a single attack.\n'
+' - Disarm: remove an opponent’s weapon.\n'
+' - Throw: reposition an opponent or drop them to the ground. '
,

' Get 1 Edge, but you underestimate your opponents, who may be more numerous or skilled than you first assumed. The GM makes a Move. \nEdges:\n'
+' - Block: avoid a melee attack.\n'
+' - Roundhouse strike: Engage in Combat against several opponents surrounding you, counting as a single attack.\n'
+' - Disarm: remove an opponent’s weapon.\n'
+' - Throw: reposition an opponent or drop them to the ground. '
]



,'officer' : [
'# Officer'
,

' Get 3 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Attack!: One ally gets +2 to their next roll to Engage in Combat.\n'
+' - Coordinate fire!: All allies get +1 to their next roll to Engage in Combat with firearms while in the fight.\n'
+' - Aim for the head!: You or one of your allies’ Engage in Combat deals +1 Harm.\n'
+' - Take cover!: You or an ally receive 2 Armor against a ranged attack. '
,

' Get 2 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Attack!: One ally gets +2 to their next roll to Engage in Combat.\n'
+' - Coordinate fire!: All allies get +1 to their next roll to Engage in Combat with firearms while in the fight.\n'
+' - Aim for the head!: You or one of your allies’ Engage in Combat deals +1 Harm.\n'
+' - Take cover!: You or an ally receive 2 Armor against a ranged attack. '
,

' You misjudge the situation. Choose whether you have put yourself or one of your allies in harm’s way. The GM makes a Move for your opponent. '
]



,'ruthless' : [
'# Ruthless'
,

' Get 3 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Human shield: force them to take all the Harm from one attack for you.\n'
+' - Bait: expose someone to danger so you can flank an enemy (deal +1 Harm).\n'
+' - Sacrifice: Leave them to the enemy while you slip away. '
,

' Get 2 Edges. \nEdges:\n'
+' - Human shield: force them to take all the Harm from one attack for you.\n'
+' - Bait: expose someone to danger so you can flank an enemy (deal +1 Harm).\n'
+' - Sacrifice: Leave them to the enemy while you slip away. '
,

' Things turns out in a bad way for you instead. The GM makes a Move. '
]



,'sniper' : [
'# Sniper'
,

' The shot finds its target. Choose two options. \nOptions:\n'
+' - Deal +1 Harm.\n'
+' - Hit another target as well.\n'
+' - Immobilize your target.\n'
+' - Get the target to lose control of something.\n'
+' - You don’t reveal your position. '
,

' The shot finds its target. Choose one option. \nOptions:\n'
+' - Deal +1 Harm.\n'
+' - Hit another target as well.\n'
+' - Immobilize your target.\n'
+' - Get the target to lose control of something.\n'
+' - You don’t reveal your position. '
,

' The shot didn’t go where you intended it to, or you reveal your position to the enemy – expect witnesses, opponents pursuing you as you leave the scene, or other problems. The GM makes a Move. '
]



,'streetfighter' : [
'# Streetfighter'
,

' Get 3 Edges. You may spend them any time during the scene. \nEdges:\n'
+' - Dodge: avoid an attack.\n'
+' - Flurry of blows: take +2 on your roll to attack an opponent.\n'
+' - Dirty strike: momentarily stun an opponent by painfully striking them, e.g. on the eye, crotch, or ear... '
,

' Get 2 Edges, but the GM also gets to pick one complication:\n'
+' - You risk losing control during the fight (Keep it Together to prevent it).\n'
+' - You earn an enemy, who will try to get back at you later. \nEdges:\n'
+' - Dodge: avoid an attack.\n'
+' - Flurry of blows: take +2 on your roll to attack an opponent.\n'
+' - Dirty strike: momentarily stun an opponent by painfully striking them, e.g. on the eye, crotch, or ear... '
,

' You’re unfocused and lose control. The GM makes a Move. '
]



,'survivalinstinct' : [
'# Survival Instinct'
,

' You ignore your injuries until the conflict is over, as well as choose one:\n'
+' - Viciousness: +1 ongoing to Engage in Combat rolls for the remainder of the fight.\n'
+' - Adrenaline rush: +1 ongoing to Endure Injury rolls for the remainder of the fight. '
,

' You ignore your injuries until the conflict is over. '
,

' You overexert yourself and after a few moments your injuries cause you to pass out and collapse. After your next action, the GM decides when and how you pass out. '
]



,'arcaneresearcher' : [
'# Arcane Researcher'
,

' Whenever you venture into alternate planes of existence or meet entities from other dimensions, you may declare that you have read about this dimension or creature before. Ask the GM what you learned from your past studies. '
,

' Whenever you venture into alternate planes of existence or meet entities from other dimensions, you may declare that you have read about this dimension or creature before. Ask the GM what you learned from your past studies. '
,

' Whenever you venture into alternate planes of existence or meet entities from other dimensions, you may declare that you have read about this dimension or creature before. Ask the GM what you learned from your past studies. '
]



,'atanycost' : [
'# At any Cost'
,

' Whenever you truly desire something, you may take +2 to a roll by decreasing Stability (−2). '
,

' Whenever you truly desire something, you may take +2 to a roll by decreasing Stability (−2). '
,

' Whenever you truly desire something, you may take +2 to a roll by decreasing Stability (−2). '
]



,'codeofhonor' : [
'# Code of Honor'
,

' You abide by a strict code of honor. Decide its nature. Whenever you take risks or make sacrifices for your code of honor, gain Stability (+1). '
,

' You abide by a strict code of honor. Decide its nature. Whenever you take risks or make sacrifices for your code of honor, gain Stability (+1). '
,

' You abide by a strict code of honor. Decide its nature. Whenever you take risks or make sacrifices for your code of honor, gain Stability (+1). '
]



,'deadshot' : [
'# Dead Shot'
,

' You are a seasoned marksman. Any Harm you deal with a firearm is considered +1 Harm. '
,

' You are a seasoned marksman. Any Harm you deal with a firearm is considered +1 Harm. '
,

' You are a seasoned marksman. Any Harm you deal with a firearm is considered +1 Harm. '
]



,'desperate' : [
'# Desperate'
,

' Whenever you try to make it through overwhelming odds, take +1 on all rolls until you’re clear of the threat. '
,

' Whenever you try to make it through overwhelming odds, take +1 on all rolls until you’re clear of the threat. '
,

' Whenever you try to make it through overwhelming odds, take +1 on all rolls until you’re clear of the threat. '
]



,'divinechampion' : [
'# Divine Champion'
,

' Whenever you fight your deity’s enemies or fight to protect a sacred object, you do +1 Harm and take +1 to Endure Injury. If you lose such a battle, your deity becomes irate, and you take −1 ongoing to all actions related to your deity until you have atoned for your failure. '
,

' Whenever you fight your deity’s enemies or fight to protect a sacred object, you do +1 Harm and take +1 to Endure Injury. If you lose such a battle, your deity becomes irate, and you take −1 ongoing to all actions related to your deity until you have atoned for your failure. '
,

' Whenever you fight your deity’s enemies or fight to protect a sacred object, you do +1 Harm and take +1 to Endure Injury. If you lose such a battle, your deity becomes irate, and you take −1 ongoing to all actions related to your deity until you have atoned for your failure. '
]



,'elitesport' : [
'# Elite Sport'
,

' You’ve competed professionally in a sport, through which you have received stipends to fund your studies. Choose a sport:\n'
+' - Fencing: When using swords, you can make the attack, Riposte [3], [Distance: arm, attack immediately after parrying], and you have a rapier [Stabbing weapon] at home.\n'
+' - Baseball/Cricket/Football/Soccer/Tennis: You take +1 ongoing while running, throwing, or catching objects.\n'
+' - Ice hockey: You take +1 to rolls to Endure Injury against close combat attacks. '
,

' You’ve competed professionally in a sport, through which you have received stipends to fund your studies. Choose a sport:\n'
+' - Fencing: When using swords, you can make the attack, Riposte [3], [Distance: arm, attack immediately after parrying], and you have a rapier [Stabbing weapon] at home.\n'
+' - Baseball/Cricket/Football/Soccer/Tennis: You take +1 ongoing while running, throwing, or catching objects.\n'
+' - Ice hockey: You take +1 to rolls to Endure Injury against close combat attacks. '
,

' You’ve competed professionally in a sport, through which you have received stipends to fund your studies. Choose a sport:\n'
+' - Fencing: When using swords, you can make the attack, Riposte [3], [Distance: arm, attack immediately after parrying], and you have a rapier [Stabbing weapon] at home.\n'
+' - Baseball/Cricket/Football/Soccer/Tennis: You take +1 ongoing while running, throwing, or catching objects.\n'
+' - Ice hockey: You take +1 to rolls to Endure Injury against close combat attacks. '
]



,'enduretrauma' : [
'# Endure Trauma'
,

' You are not as easily affected by trauma as others. Whenever you reduce Stability, you always lose 1 fewer level than normal. '
,

' You are not as easily affected by trauma as others. Whenever you reduce Stability, you always lose 1 fewer level than normal. '
,

' You are not as easily affected by trauma as others. Whenever you reduce Stability, you always lose 1 fewer level than normal. '
]



,'eyeforaneye' : [
'# Eye for an Eye'
,

' Whenever you suffer a serious or critical injury, name the person you feel is responsible. You get +2 ongoing to all rolls against them, forever. All rolls targeting the person count, but rolls targeting the person’s family, friends, minions, and property only count if the GM feels they’re applicable. '
,

' Whenever you suffer a serious or critical injury, name the person you feel is responsible. You get +2 ongoing to all rolls against them, forever. All rolls targeting the person count, but rolls targeting the person’s family, friends, minions, and property only count if the GM feels they’re applicable. '
,

' Whenever you suffer a serious or critical injury, name the person you feel is responsible. You get +2 ongoing to all rolls against them, forever. All rolls targeting the person count, but rolls targeting the person’s family, friends, minions, and property only count if the GM feels they’re applicable. '
]



,'goodsamaritan' : [
'# Good Samaritan'
,

' Whenever you help another at your own expense, gain Stability (+1). '
,

' Whenever you help another at your own expense, gain Stability (+1). '
,

' Whenever you help another at your own expense, gain Stability (+1). '
]



,'grittedteeth' : [
'# Gritted Teeth'
,

' Abuse, violence, self-harm, and assaults have become familiar, and the pain hardly affects you at all anymore. You suffer no penalties from wounds, whether serious or critical. '
,

' Abuse, violence, self-harm, and assaults have become familiar, and the pain hardly affects you at all anymore. You suffer no penalties from wounds, whether serious or critical. '
,

' Abuse, violence, self-harm, and assaults have become familiar, and the pain hardly affects you at all anymore. You suffer no penalties from wounds, whether serious or critical. '
]



,'grudge' : [
'# Grudge'
,

' When someone directly or indirectly ruins your plans, you take +1 ongoing against them until you have taken revenge or received restitution of equal worth to what you lost. '
,

' When someone directly or indirectly ruins your plans, you take +1 ongoing against them until you have taken revenge or received restitution of equal worth to what you lost. '
,

' When someone directly or indirectly ruins your plans, you take +1 ongoing against them until you have taken revenge or received restitution of equal worth to what you lost. '
]



,'hardened' : [
'# Hardened'
,

' You take +1 ongoing to Endure Injury. '
,

' You take +1 ongoing to Endure Injury. '
,

' You take +1 ongoing to Endure Injury. '
]



,'jaded' : [
'# Jaded'
,

' Whenever you roll (10–14) to Keep it Together, you may suppress your emotions and postpone their effects until the next scene. '
,

' Whenever you roll (10–14) to Keep it Together, you may suppress your emotions and postpone their effects until the next scene. '
,

' Whenever you roll (10–14) to Keep it Together, you may suppress your emotions and postpone their effects until the next scene. '
]



,'manipulative' : [
'# Manipulative'
,

' Whenever you do someone a favor or learn one of their secrets, you may later choose one of the options below, by reminding them of your prior services or hint at the secret you know:\n'
+' - Take +2 to Influence them.\n'
+' - Take +2 to Hinder them. '
,

' Whenever you do someone a favor or learn one of their secrets, you may later choose one of the options below, by reminding them of your prior services or hint at the secret you know:\n'
+' - Take +2 to Influence them.\n'
+' - Take +2 to Hinder them. '
,

' Whenever you do someone a favor or learn one of their secrets, you may later choose one of the options below, by reminding them of your prior services or hint at the secret you know:\n'
+' - Take +2 to Influence them.\n'
+' - Take +2 to Hinder them. '
]



,'opportunist' : [
'# Opportunist'
,

' Whenever you sacrifice someone else to further your own goals, gain Stability (+1). '
,

' Whenever you sacrifice someone else to further your own goals, gain Stability (+1). '
,

' Whenever you sacrifice someone else to further your own goals, gain Stability (+1). '
]



,'rage' : [
'# Rage'
,

' When in combat, you may awaken your inner rage. Lose Stability (−1) and mark 1 Rage. Every time you get a wound and every time you defeat a foe, increase Rage (+1). Rage lasts until the end of the combat.During combat, you may spend 1 Rage to choose 1 Edge:\n'
+' - Brutal assault: take +1 Harm to your attack.\n'
+' - Ignore the pain: take +2 to Endure Injury.\n'
+' - Lost in frenzy: shake off and ignore psychological or supernatural influence. '
,

' When in combat, you may awaken your inner rage. Lose Stability (−1) and mark 1 Rage. Every time you get a wound and every time you defeat a foe, increase Rage (+1). Rage lasts until the end of the combat.During combat, you may spend 1 Rage to choose 1 Edge:\n'
+' - Brutal assault: take +1 Harm to your attack.\n'
+' - Ignore the pain: take +2 to Endure Injury.\n'
+' - Lost in frenzy: shake off and ignore psychological or supernatural influence. '
,

' When in combat, you may awaken your inner rage. Lose Stability (−1) and mark 1 Rage. Every time you get a wound and every time you defeat a foe, increase Rage (+1). Rage lasts until the end of the combat.During combat, you may spend 1 Rage to choose 1 Edge:\n'
+' - Brutal assault: take +1 Harm to your attack.\n'
+' - Ignore the pain: take +2 to Endure Injury.\n'
+' - Lost in frenzy: shake off and ignore psychological or supernatural influence. '
]



,'sealedfate' : [
'# Sealed Fate'
,

' (requires the Disadvantage Condemned) Whenever you are dealt a Critical Wound, you may mark 1 Time from Condemned to immediately stabilize the Wound. Whenever you die, mark 2 Time from Condemned and reawaken, injured and weak, but alive. All your Wounds will be stabilized. '
,

' (requires the Disadvantage Condemned) Whenever you are dealt a Critical Wound, you may mark 1 Time from Condemned to immediately stabilize the Wound. Whenever you die, mark 2 Time from Condemned and reawaken, injured and weak, but alive. All your Wounds will be stabilized. '
,

' (requires the Disadvantage Condemned) Whenever you are dealt a Critical Wound, you may mark 1 Time from Condemned to immediately stabilize the Wound. Whenever you die, mark 2 Time from Condemned and reawaken, injured and weak, but alive. All your Wounds will be stabilized. '
]



,'thirstforknowledge' : [
'# Thirst for Knowledge'
,

' Whenever you learn new information about alternate planes of existence, a supernatural entity, or a Higher Power, gain Stability (+1). '
,

' Whenever you learn new information about alternate planes of existence, a supernatural entity, or a Higher Power, gain Stability (+1). '
,

' Whenever you learn new information about alternate planes of existence, a supernatural entity, or a Higher Power, gain Stability (+1). '
]



,'tothelastbreath' : [
'# To the Last Breath'
,

' (requires the Disadvantage Condemned) When you refuse to give in even if the odds turn against you, mark 1 Time to reroll the dice. '
,

' (requires the Disadvantage Condemned) When you refuse to give in even if the odds turn against you, mark 1 Time to reroll the dice. '
,

' (requires the Disadvantage Condemned) When you refuse to give in even if the odds turn against you, mark 1 Time to reroll the dice. '
]



,'watchers' : [
'# Watchers'
,

' You are being watched over and protected by a group of mysterious people who intend on keeping you alive for their own obscure purposes. Whenever you are in mortal danger, you can activate your watchers. If you do, the GM takes 1 Hold. The watchers act as a small/medium/ large gang (2/3/3 Harm, 5/10/15 Wounds), dependent on how powerful the threat is. Their sole motivation is to keep you out of harm’s reach. The GM can also spend Hold on the watchers’ behalf to let them make a Move against you. '
,

' You are being watched over and protected by a group of mysterious people who intend on keeping you alive for their own obscure purposes. Whenever you are in mortal danger, you can activate your watchers. If you do, the GM takes 1 Hold. The watchers act as a small/medium/ large gang (2/3/3 Harm, 5/10/15 Wounds), dependent on how powerful the threat is. Their sole motivation is to keep you out of harm’s reach. The GM can also spend Hold on the watchers’ behalf to let them make a Move against you. '
,

' You are being watched over and protected by a group of mysterious people who intend on keeping you alive for their own obscure purposes. Whenever you are in mortal danger, you can activate your watchers. If you do, the GM takes 1 Hold. The watchers act as a small/medium/ large gang (2/3/3 Harm, 5/10/15 Wounds), dependent on how powerful the threat is. Their sole motivation is to keep you out of harm’s reach. The GM can also spend Hold on the watchers’ behalf to let them make a Move against you. '
]



,'workaholic' : [
'# Workaholic'
,

' Whenever you create something or carry out an experiment, gain Stability (+1). '
,

' Whenever you create something or carry out an experiment, gain Stability (+1). '
,

' Whenever you create something or carry out an experiment, gain Stability (+1). '
]



,'worldly' : [
'# Worldly'
,

' Whenever you arrive at a new location in the mundane world, decide whether you have been here before, and if so, name some detail about the place significant to you. Also, decide if you met someone there and what you left behind. The GM will say what has changed since then. '
,

' Whenever you arrive at a new location in the mundane world, decide whether you have been here before, and if so, name some detail about the place significant to you. Also, decide if you met someone there and what you left behind. The GM will say what has changed since then. '
,

' Whenever you arrive at a new location in the mundane world, decide whether you have been here before, and if so, name some detail about the place significant to you. Also, decide if you met someone there and what you left behind. The GM will say what has changed since then. '
]



,'services' : [
'# Services'
,

' The debt remains the same. Regardless of the outcome, the PC can ask the entity for one of the following:\n'
+' - The answer to a query.\n'
+' - Guidance to a location in one of the dimensions.\n'
+' - A weapon the PC can use against their enemy (this can also constitute a creature, knowledge, or direct interference on part of the entity).\n'
+' - The opening of a portal to one of the dimensions. '
,

' The debt increases by +1. Regardless of the outcome, the PC can ask the entity for one of the following:\n'
+' - The answer to a query.\n'
+' - Guidance to a location in one of the dimensions.\n'
+' - A weapon the PC can use against their enemy (this can also constitute a creature, knowledge, or direct interference on part of the entity).\n'
+' - The opening of a portal to one of the dimensions. '
,

' The debt immediately goes to +5. Regardless of the outcome, the PC can ask the entity for one of the following:\n'
+' - The answer to a query.\n'
+' - Guidance to a location in one of the dimensions.\n'
+' - A weapon the PC can use against their enemy (this can also constitute a creature, knowledge, or direct interference on part of the entity).\n'
+' - The opening of a portal to one of the dimensions. '
]



,'badreputation' : [
'# Bad Reputation'
,

' You blend in. Nobody is out to get you. '
,

' You have been recognized. The GM takes 1 Hold. The GM can spend Hold to make a Move representing how your bad reputation sticks to you. For example, people might react with fear and suspicion towards you, a lynch mob forms to bring you to justice, your property is vandalized, your allies turn against you, and you can lose your job, agreements, and relationships. '
,

' Several people have recognized you. Anger and fear control their actions. The GM takes 3 Hold. The GM can spend Hold to make a Move representing how your bad reputation sticks to you. For example, people might react with fear and suspicion towards you, a lynch mob forms to bring you to justice, your property is vandalized, your allies turn against you, and you can lose your job, agreements, and relationships. '
]



,'broken' : [
'# Broken'
,

' Some experience in your past has broken your psyche so badly you’ve been unable to recuperate from it. As a result, your Stability can never increase beyond Distressed (6). '
,

' Some experience in your past has broken your psyche so badly you’ve been unable to recuperate from it. As a result, your Stability can never increase beyond Distressed (6). '
,

' Some experience in your past has broken your psyche so badly you’ve been unable to recuperate from it. As a result, your Stability can never increase beyond Distressed (6). '
]



,'competitor' : [
'# Competitor'
,

' You are safe from your competitor, for the moment. '
,

' You have been careless. Your competitor may strike against you. The GM takes 1 Hold. The GM can spend Hold to make Moves for your competitor. For example, your competitor may take control of some of your business dealings, learn one of your secrets, sabotagesone of your assets, or harms or buys off someone you care for and trust. '
,

' You hand your competitor a golden opportunity, and they move against your interests. The GM takes 3 Hold. The GM can spend Hold to make Moves for your competitor. For example, your competitor may take control of some of your business dealings, learn one of your secrets, sabotagesone of your assets, or harms or buys off someone you care for and trust. '
]



,'condemned' : [
'# Condemned'
,

' You still have some time remaining. '
,

' Your fate approaches. The GM chooses one of the following options: \n'
+' - The player marks 1 Time. \n'
+' - You’re tortured by dreams or visions of your fate. Reduce Stability (−2). \n'
+' - You’re haunted by the entity or event that sealed your fate. \n'
+' - Someone in your vicinity is negatively affected by your fate. \n'
+' - Something provides you with false hope of escaping your fate. '
,

' Your end approaches. The GM holds two options from the list below or marks 2 Time. When you finally run out of Time, you meet your ultimate fate. \n'
+' - The player marks 1 Time. \n'
+' - You’re tortured by dreams or visions of your fate. Reduce Stability (−2). \n'
+' - You’re haunted by the entity or event that sealed your fate. \n'
+' - Someone in your vicinity is negatively affected by your fate. \n'
+' - Something provides you with false hope of escaping your fate. '
]



,'cursed' : [
'# Cursed'
,

' You temporarily avoid the curse’s influence. '
,

' The GM takes 1 Hold. The GM can spend Hold to make a Move for the curse. For example, you or someone you care about have an accident, something of yours is taken from you, you experience terrifying visions, or you’re forced to take certain actions with risk of dire consequences, if you refuse. '
,

' The GM takes 3 Hold. The GM can spend Hold to make a Move for the curse. For example, you or someone you care about have an accident, something of yours is taken from you, you experience terrifying visions, or you’re forced to take certain actions with risk of dire consequences, if you refuse. '
]



,'depression' : [
'# Depression'
,

' You remain in control. '
,

' You experience temporary anxiety, decreased self-confidence, or lack of will. You take −1 to your next roll. '
,

' You succumb to the sense of hopelessness or blame and punish yourself; reduce Stability (−2). Your lethargy and self-destructive urges do not go away until you numb your depression with medicine, drugs, or alcohol. '
]



,'drugaddict' : [
'# Drug Addict'
,

' You are in control of the urge, for now. '
,

' The GM takes 1 Hold. The GM may spend Hold to make a Move for your addiction. For example, you cannot resist using the drug, run out of drugs, become indebted to a dangerous person, put yourself in danger while under the influence of drugs, or ruin something important to you – like a relationship – while under the influence. '
,

' The GM takes 3 Hold. The GM may spend Hold to make a Move for your addiction. For example, you cannot resist using the drug, run out of drugs, become indebted to a dangerous person, put yourself in danger while under the influence of drugs, or ruin something important to you – like a relationship – while under the influence. '
]



,'experimentgonewrong' : [
'# Experiment Gone Wrong'
,

' Your experiment leaves you alone. '
,

' Your experiment is close on your heels. The GM takes 1 Hold. The GM can spend Hold to make Moves on the experiment’s behalf. For example, the experiment gives you a lead on the Truth, sabotages or otherwise disrupts your research, demands something from you under threat of retribution, or kidnaps someone you care for – possibly returning them dead or transformed. '
,

' Your experiment is in your vicinity and acts against you. The GM takes 3 Hold. The GM can spend Hold to make Moves on the experiment’s behalf. For example, the experiment gives you a lead on the Truth, sabotages or otherwise disrupts your research, demands something from you under threat of retribution, or kidnaps someone you care for – possibly returning them dead or transformed. '
]



,'fanatic' : [
'# Fanatic'
,

' You can keep your emotions in check. '
,

' You become angry, confused, or frustrated. You take −1 to your next roll. '
,

' You are forced to choose between taking steps to changing the person or situation to adhere to your ideology, or reduce Stability (−2). '
]



,'greedy' : [
'# Greedy'
,

' You keep your greed in check. '
,

' The black void inside shrieks for more. As long as the opportunity exists and you do not take it, you suffer −1 ongoing to any rolls you make. '
,

' You must take advantage of every opportunity to further your wealth, or reduce Stability (−2). '
]



,'guilt' : [
'# Guilt'
,

' Your guilt isn’t on your mind at the moment. '
,

' You are reminded of your guilt. The GM takes 1 Hold. The GM can spend Hold to make Moves for your guilt. For example, relatives of the people you’ve hurt seek you out, demons and other creatures are attracted by your guilt, the dead haunt you with nightmares or visions, or you fall victim to anxiety and self-doubt. '
,

' Your guilt catches up to you. The GM takes 3 Hold. The GM can spend Hold to make Moves for your guilt. For example, relatives of the people you’ve hurt seek you out, demons and other creatures are attracted by your guilt, the dead haunt you with nightmares or visions, or you fall victim to anxiety and self-doubt. '
]



,'harassed' : [
'# Harassed'
,

' You’ve managed to keep clear of harassment. '
,

' The GM takes 1 Hold. The GM can spend Hold to make Moves for the harassers. For example, someone destroys your property or possessions, you are bullied and attacked by people with a prejudice against you, the authorities forcefully take something from you (rights, property, assets), someone you care about is harmed for associating with you, or you are denied your basic rights due to your identity. '
,

' The GM takes 3 Hold. The GM can spend Hold to make Moves for the harassers. For example, someone destroys your property or possessions, you are bullied and attacked by people with a prejudice against you, the authorities forcefully take something from you (rights, property, assets), someone you care about is harmed for associating with you, or you are denied your basic rights due to your identity. '
]



,'haunted' : [
'# Haunted'
,

' The entity leaves you alone. '
,

' The GM takes 1 Hold. The GM can spend Hold to make a Move for the entity. For example, it requests a service from you and threatens retribution if you refuse, the entity possesses your body for the night, or the entity reveals a clue of what it is and what it wants from you. '
,

' The GM takes 3 Hold. The GM can spend Hold to make a Move for the entity. For example, it requests a service from you and threatens retribution if you refuse, the entity possesses your body for the night, or the entity reveals a clue of what it is and what it wants from you. '
]



,'infirm' : [
'# Infirm'
,

' Your condition is under control. '
,

' Your condition triggers, causing pain and daze (−1 to all rolls until the scene ends). '
,

' Your condition is aggravated with life threatening results (Endure Injury with 2 Harm). '
]



,'involuntarymedium' : [
'# Involuntary Medium'
,

' You resist the possession. '
,

' The entity gains influence over you. The GM takes 1 Hold. The GM can spend Hold to make Moves for the being possessing you. For example, the entity may give you a vision, make use of your body, communicate with or through you, try to harm someone else through you, follow you unseen, demand something from you, or drag you into another dimension. '
,

' The entity gains control over you. The GM takes 3 Hold. The GM can spend Hold to make Moves for the being possessing you. For example, the entity may give you a vision, make use of your body, communicate with or through you, try to harm someone else through you, follow you unseen, demand something from you, or drag you into another dimension. '
]



,'jealousy' : [
'# Jealousy'
,

' You maintain control over your jealousy. '
,

' You’re afflicted by jealousy and take −1 ongoing for as long as you remain in the subject’s vicinity, and you do not suppress your jealous desires. '
,

' Your jealousy takes hold of you. You must Keep it Together to refrain from harming, destroying, or stealing from the subject of your jealousy. '
]



,'liar' : [
'# Liar'
,

' You have kept your lies tangle-free. '
,

' You’ve told one too many lies. The GM takes 1 Hold. The GM can spend Hold whenever a PC encounters someone they know to ask, “What have you lied about to this person?” or to invent a troublesome lie the PC has told in the past. '
,

' Your web of lies has come completely unraveled. The GM takes 3 Hold. The GM can spend Hold whenever a PC encounters someone they know to ask, “What have you lied about to this person?” or to invent a troublesome lie the PC has told in the past. '
]



,'lostidentity' : [
'# Lost Identity'
,

' You repress your true identity, remaining in the present. '
,

' Your true identity is catching up to you. The GM takes 1 Hold. The GM can spend Hold to make Moves for your true  identity. For example, you recognize unknown people or places, organizations or individuals from your past life get in touch with you, your old identity influences your thought patterns or actions, or you suffer traumatic flashbacks. '
,

' Your true identity resurfaces. The GM takes 3 Hold. The GM can spend Hold to make Moves for your true  identity. For example, you recognize unknown people or places, organizations or individuals from your past life get in touch with you, your old identity influences your thought patterns or actions, or you suffer traumatic flashbacks. '
]



,'marked' : [
'# Marked'
,

' You are still in control. '
,

' You feed the darkness. The GM takes 1 Hold. The GM can spend Hold to make Moves for the darkness living inside of you. For example, the darkness feeds on your life energy to sustain itself, forces you to commit murder in order to replenish its life energy, takes charge of your body and leaves you with only memory fragments of what transpired, forces you to harm someone in your vicinity, or temporarily transforms your body into something inhuman. You may have to Keep it Together to resist the darkness’ influence. '
,

' The darkness gains power over you. The GM takes 3 Hold. The GM can spend Hold to make Moves for the darkness living inside of you. For example, the darkness feeds on your life energy to sustain itself, forces you to commit murder in order to replenish its life energy, takes charge of your body and leaves you with only memory fragments of what transpired, forces you to harm someone in your vicinity, or temporarily transforms your body into something inhuman. You may have to Keep it Together to resist the darkness’ influence. '
]



,'mentalcompulsion' : [
'# Mental Compulsion'
,

' You control your compulsions and can focus on other things. '
,

' You become distracted and take −1 ongoing to all rolls until you have removed yourself from the situation or succumbed to your compulsion, taking any actions it demands of you. '
,

' You become completely obsessed with your compulsion. If you focus on anything else, reduce Stability (−2). '
]



,'nemesis' : [
'# Nemesis'
,

' You are safe from your nemesis for the moment. '
,

' You have been careless and your nemesis moves against you. The GM takes 1 Hold. The GM can spend Hold to make Moves on behalf of your nemesis. For example, your nemesis may strike when you’re alone, use secrets they’ve uncovered to extort you, intimidate you, hire henchmen to capture you, or attack someone or something you hold dear. '
,

' You have compromised your position and your nemesis strikes against you in full force. The GM takes 3 Hold. The GM can spend Hold to make Moves on behalf of your nemesis. For example, your nemesis may strike when you’re alone, use secrets they’ve uncovered to extort you, intimidate you, hire henchmen to capture you, or attack someone or something you hold dear. '
]



,'nightmares' : [
'# Nightmares'
,

' You sleep in peace. '
,

' The nightmares torment you. The GM may make a Move for your nightmares. For example, you are unable to sleep at all during the night (−1 ongoing until you sleep), something follows you back into reality, the nightmares provide you insight into the Truth, or you are forced to process some trauma (Keep it Together) when you wake up. '
,

' The nightmares take over completely. You are trapped in the dream until you find a way to wake up, and everything that happens there also directly affects your sleeping body. '
]



,'oathofrevenge' : [
'# Oath of Revenge'
,

' You remain in control of your vengeful nature and can act rationally. '
,

' You can’t focus on anything, other than the target of your vengeance. Take −1 ongoing until the target’s involvement in the scene ends. '
,

' You become obsessed and can act only to further your revenge. Doing anything else requires you roll Keep it Together. Your obsession cannot be assuaged while the target remains in the same scene with you. '
]



,'objectofdesire' : [
'# Object of Desire'
,

' The desire is not awakened at this moment. '
,

' Someone becomes desirous of you. The GM takes 1 Hold. The GM can spend Hold to ignite a person’s desires, influencing their behavior. For example, someone can be afflicted with an uncontrollable passion for you, attempt to force themselves on you, strongly proposition you, become intensely jealous of you, or harm themselves or someone else because of their desire of you. '
,

' A strong desire is awakened in one or several people. The GM takes 3 Hold. The GM can spend Hold to ignite a person’s desires, influencing their behavior. For example, someone can be afflicted with an uncontrollable passion for you, attempt to force themselves on you, strongly proposition you, become intensely jealous of you, or harm themselves or someone else because of their desire of you. '
]



,'obsession' : [
'# Obsession'
,

' You overcome your obsession for the moment. '
,

' Your obsession influences your behavior. The GM takes 1 Hold. The GM can spend Hold to let your obsession creep into your daily life. You may be forced to choose between either engaging in your obsession or losing Stability. You may forget about important tasks and chores, miss meetings, or neglect your interpersonal relationships to solely focus on your obsession. Your obsession may even influence your dreams, giving you visions and revelations. In turn, the object of your obsession may also take note of you and try to stop your investigations. '
,

' Your obsession takes over completely. The GM takes 3 Hold. The GM can spend Hold to let your obsession creep into your daily life. You may be forced to choose between either engaging in your obsession or losing Stability. You may forget about important tasks and chores, miss meetings, or neglect your interpersonal relationships to solely focus on your obsession. Your obsession may even influence your dreams, giving you visions and revelations. In turn, the object of your obsession may also take note of you and try to stop your investigations. '
]



,'owned' : [
'# Owned'
,

' For the moment, you are safe. '
,

' Your former owner picks up your scent. The GM takes 1 Hold. The GM can spend Hold to make Moves for your former owner. For example, they appear unexpectedly to convince you to return, send henchmen after you, kidnap or harm someone you care about, directly threaten you, destroy something important to you, try to mutilate you so nobody else would want you, or kill you outright so nobody else can have you. '
,

' Your owner finds you. The GM takes 3 Hold. The GM can spend Hold to make Moves for your former owner. For example, they appear unexpectedly to convince you to return, send henchmen after you, kidnap or harm someone you care about, directly threaten you, destroy something important to you, try to mutilate you so nobody else would want you, or kill you outright so nobody else can have you. '
]



,'phobia' : [
'# Phobia'
,

' You harbor an overpowering fear of something. Choose the stimulus that frightens you. Whenever you’re confronted by the object of your phobia, you must Keep it Together. '
,

' You harbor an overpowering fear of something. Choose the stimulus that frightens you. Whenever you’re confronted by the object of your phobia, you must Keep it Together. '
,

' You harbor an overpowering fear of something. Choose the stimulus that frightens you. Whenever you’re confronted by the object of your phobia, you must Keep it Together. '
]



,'rationalist' : [
'# Rationalist'
,

' You refuse to believe in anything not confirmed as fact by modern science, even when it is right in front of you. In addition to the standard effects, whenever you See Through the Illusion and whenever the Illusion shatters, the GM may choose one option: \n'
+' - Your presence nurtures the Illusion, making it more powerful and impenetrable. \n'
+' - Your bewildered psyche starts creating mirror images of familiar places and people in the Illusion. \n'
+' - You attract extradimensional entities. \n'
+' - You consciously deny what you see, even to your own detriment. '
,

' You refuse to believe in anything not confirmed as fact by modern science, even when it is right in front of you. In addition to the standard effects, whenever you See Through the Illusion and whenever the Illusion shatters, the GM may choose one option: \n'
+' - Your presence nurtures the Illusion, making it more powerful and impenetrable. \n'
+' - Your bewildered psyche starts creating mirror images of familiar places and people in the Illusion. \n'
+' - You attract extradimensional entities. \n'
+' - You consciously deny what you see, even to your own detriment. '
,

' You refuse to believe in anything not confirmed as fact by modern science, even when it is right in front of you. In addition to the standard effects, whenever you See Through the Illusion and whenever the Illusion shatters, the GM may choose one option: \n'
+' - Your presence nurtures the Illusion, making it more powerful and impenetrable. \n'
+' - Your bewildered psyche starts creating mirror images of familiar places and people in the Illusion. \n'
+' - You attract extradimensional entities. \n'
+' - You consciously deny what you see, even to your own detriment. '
]



,'repressedmemories' : [
'# Repressed Memories'
,

' You continue to suppress the memories. '
,

' The memories partly resurface, taking the form of flashbacks and/or hallucinations. You must Keep it Together. '
,

' You are overwhelmed by your repressed memories, completely losing yourself to them. The GM makes a hard Move and you reduce Stability (−2). '
]



,'rival' : [
'# Rival'
,

' All clear; your rival makes no moves against you. '
,

' You’ve given your rival an opportunity. The GM takes 1 Hold. The GM can spend Hold to make a Move on behalf of your rival. For example, the rival may get an important person on their side, sabotage one of your projects, extort you with evidence damaging to your reputation, or take desperate measures to get rid of you permanently. '
,

' You’ve handed your rival whatever they needed to completely undermine you. The GM takes 3 Hold. The GM can spend Hold to make a Move on behalf of your rival. For example, the rival may get an important person on their side, sabotage one of your projects, extort you with evidence damaging to your reputation, or take desperate measures to get rid of you permanently. '
]



,'schizophrenia' : [
'# Schizophrenia'
,

' You maintain control of your insanity. '
,

' The GM takes 1 Hold. The GM may spend Hold to make a Move for your schizophrenia. For example, one of your hallucinations takes on physical form, you view your current surroundings as being hostile to you, you’re afflicted by terrifying hallucinations, you’re subjected to dark visions (true or false), or someone in your vicinity turns out to not actually be real. '
,

' Schizophrenia overtakes you. The GM takes 3 Hold. The GM may spend Hold to make a Move for your schizophrenia. For example, one of your hallucinations takes on physical form, you view your current surroundings as being hostile to you, you’re afflicted by terrifying hallucinations, you’re subjected to dark visions (true or false), or someone in your vicinity turns out to not actually be real. '
]



,'sexualneurosis' : [
'# Sexual Neurosis'
,

' You can control your urges. '
,

' Choose between having sex with the person or reduce your Stability (−1). '
,

' You cannot resist having sex with the person and the GM chooses one option: \n'
+' - You hurt, or you are hurt by, your sexual partner (physically or psychologically). \n'
+' - The boundaries between dimensions are weakened; an entity from beyond catches the scent of you or your lover. \n'
+' - Your sexual partner becomes obsessed with you and starts stalking you. '
]



,'stalker' : [
'# Stalker'
,

' You are safe for now. '
,

' Your enemies are on to you. The GM takes 1 Hold. The GM can spend Hold to make a Move for your pursuers. For example, a trusted associate has been paid off by them, one of your loved ones or allies disappears, something you are trying to do is undermined by your enemies, or they try to actively hurt you. '
,

' Your enemies have caught up to you. The GM takes 3 Hold. The GM can spend Hold to make a Move for your pursuers. For example, a trusted associate has been paid off by them, one of your loved ones or allies disappears, something you are trying to do is undermined by your enemies, or they try to actively hurt you. '
]



,'victimofpassion' : [
'# Victim of Passion'
,

' You keep your passion in check. '
,

' The passion awakens within you. The GM takes 1 Hold. The GM can spend Hold to let your passion steer your actions. For example, you yearn uncontrollably for the subject of your passion – you must seek it out or reduce Stability (−2), your desire drags the subject of your passion into your dreams (perhaps trapping them there), your passion becomes tainted with jealousy and anger – making you want to control and damage it (Keep it Together to resist), your longing leaves you feeble vis-à-vis the objective of this passion (−1 to all rolls while sharing the same scene), or your passion can attract creatures of lust wishing to feed off it or make pacts with you. '
,

' You are completely in the passion’s grip. The GM takes 3 Hold. The GM can spend Hold to let your passion steer your actions. For example, you yearn uncontrollably for the subject of your passion – you must seek it out or reduce Stability (−2), your desire drags the subject of your passion into your dreams (perhaps trapping them there), your passion becomes tainted with jealousy and anger – making you want to control and damage it (Keep it Together to resist), your longing leaves you feeble vis-à-vis the objective of this passion (−1 to all rolls while sharing the same scene), or your passion can attract creatures of lust wishing to feed off it or make pacts with you. '
]



,'wanted' : [
'# Wanted'
,

' You are safe, for now. '
,

' You have made a mistake. The GM takes 1 Hold. The GM can spend Hold to make a Move for the authorities. For example, your mugshot appears on the TV news and in newspapers, law enforcement officers attempt to trap and catch you, or the authorities detain and interrogate someone you care about, confiscate your possessions, or turn your friends/family against you. '
,

' All eyes are on you. The GM takes 3 Hold. The GM can spend Hold to make a Move for the authorities. For example, your mugshot appears on the TV news and in newspapers, law enforcement officers attempt to trap and catch you, or the authorities detain and interrogate someone you care about, confiscate your possessions, or turn your friends/family against you. '
]



,'performaritual' : [
'# Perform a Ritual'
,

' Choose 2 options(or 3 if Master) from the list below. Options:\n'
+' - The ritual affects other dimensions.\n'
+' - The ritual’s effects last for as long as you actively uphold them.\n'
+' - The ritual doesn’t become unstable (cannot be chosen on a –9 result).\n'
+' - Journeyman or higher: You have protection from creatures and magical energies for as long as you remain within the protective circle.\n'
+' - Adept or higher: The ritual affects several beings. '
,

' Choose 1 option(or 2 if Master). Options:\n'
+' - The ritual affects other dimensions.\n'
+' - The ritual’s effects last for as long as you actively uphold them.\n'
+' - The ritual doesn’t become unstable (cannot be chosen on a –9 result).\n'
+' - Journeyman or higher: You have protection from creatures and magical energies for as long as you remain within the protective circle.\n'
+' - Adept or higher: The ritual affects several beings. '
,

' Choose 1 option(or 2 if Master), but the ritual has unexpected consequences, making it either more powerful or weaker than anticipated, causes the magician to attract extra-dimensional beings, or the Illusion tears. The GM makes a Move. Options:\n'
+' - The ritual affects other dimensions.\n'
+' - The ritual’s effects last for as long as you actively uphold them.\n'
+' - The ritual doesn’t become unstable (cannot be chosen on a –9 result).\n'
+' - Journeyman or higher: You have protection from creatures and magical energies for as long as you remain within the protective circle.\n'
+' - Adept or higher: The ritual affects several beings. '
]



,'adept' : [
'# Adept'
,

' (requires: Journeyman) You’re starting to reach deeper insights into your school of magic. Choose 1 new Field of Expertise.  Adept Ability: Powerful. When you Perform a Ritual, you can choose this option:\n'
+' - The ritual affects several beings. '
,

' (requires: Journeyman) You’re starting to reach deeper insights into your school of magic. Choose 1 new Field of Expertise.  Adept Ability: Powerful. When you Perform a Ritual, you can choose this option:\n'
+' - The ritual affects several beings. '
,

' (requires: Journeyman) You’re starting to reach deeper insights into your school of magic. Choose 1 new Field of Expertise.  Adept Ability: Powerful. When you Perform a Ritual, you can choose this option:\n'
+' - The ritual affects several beings. '
]



,'asecondchance' : [
'# A Second Chance'
,

' You have learned an ancient ritual. When you die, you may choose to possess the body of a human victim. You must have prepared the victim in advance, and they should be kept confined in your sanctum. Your victim’s original soul doesn’t leave their body, but is merely suppressed. Take the Disadvantage Haunted. '
,

' You have learned an ancient ritual. When you die, you may choose to possess the body of a human victim. You must have prepared the victim in advance, and they should be kept confined in your sanctum. Your victim’s original soul doesn’t leave their body, but is merely suppressed. Take the Disadvantage Haunted. '
,

' You have learned an ancient ritual. When you die, you may choose to possess the body of a human victim. You must have prepared the victim in advance, and they should be kept confined in your sanctum. Your victim’s original soul doesn’t leave their body, but is merely suppressed. Take the Disadvantage Haunted. '
]



,'bewitching' : [
'# Bewitching'
,

' Choose up to 3 options. Options\n'
+' - Make your victim like you. They take +1 Relation to you.\n'
+' - Influence your victim as if you rolled a 15+.\n'
+' - Make your victim desire you. '
,

' Choose up to 2 options. Options\n'
+' - Make your victim like you. They take +1 Relation to you.\n'
+' - Influence your victim as if you rolled a 15+.\n'
+' - Make your victim desire you. '
,

' Choose 1 option, but you also make your victim become obsessed with you. They will be dying to meet you again, making every effort to do so. Options\n'
+' - Make your victim like you. They take +1 Relation to you.\n'
+' - Influence your victim as if you rolled a 15+.\n'
+' - Make your victim desire you. '
]



,'commandingvoice' : [
'# Commanding Voice'
,

' The person or creature must obey your order, unless doing so would cause them direct harm. '
,

' The person or creature must obey your order, unless doing so would expose them to danger. '
,

' The person or creature acts unpredictably. The GM determines if they resist the order, misunderstand it, carry out your instructions incorrectly, becomes angered at you, or carries out your order, but gains a magic bond to you that it will exploit later. When you give a PC an order, she must Keep it Together. If she fails, she’s unable to resist the order. '
]



,'darkaura' : [
'# Dark Aura'
,

' Choose 2 options. \nOptions:\n'
+' - You learn one of your target’s weaknesses. Take +2 to your roll against her when exploiting this weakness.\n'
+' - You can feel your target’s soul, and can ask if it has been marked or tainted by supernatural forces.\n'
+' - You curse your target. Her body starts to decompose, indicated by a Serious Wound that cannot be healed until she finds a way to break the curse. '
,

' Choose 1 option. \nOptions:\n'
+' - You learn one of your target’s weaknesses. Take +2 to your roll against her when exploiting this weakness.\n'
+' - You can feel your target’s soul, and can ask if it has been marked or tainted by supernatural forces.\n'
+' - You curse your target. Her body starts to decompose, indicated by a Serious Wound that cannot be healed until she finds a way to break the curse. '
,

' Choose 1 option, but you leave a trace of your aura with the affected person – who gains a magical bond with you. \nOptions:\n'
+' - You learn one of your target’s weaknesses. Take +2 to your roll against her when exploiting this weakness.\n'
+' - You can feel your target’s soul, and can ask if it has been marked or tainted by supernatural forces.\n'
+' - You curse your target. Her body starts to decompose, indicated by a Serious Wound that cannot be healed until she finds a way to break the curse. '
]



,'darkvision' : [
'# Dark Vision'
,

' Choose 3 Edges. You may save up to 2 until later. \nEdges:\n'
+' - Attack from cover of darkness: You can attack an opponent unexpectedly, but reveal your position when you do.\n'
+' - Dive into the shadows: You disappear into the darkness.\n'
+' - Become one with the dark: You hide yourself so well nobody can find you. '
,

' Choose 2 Edges. You may save 1 until later. \nEdges:\n'
+' - Attack from cover of darkness: You can attack an opponent unexpectedly, but reveal your position when you do.\n'
+' - Dive into the shadows: You disappear into the darkness.\n'
+' - Become one with the dark: You hide yourself so well nobody can find you. '
,

' Choose 1 Edge, but the darkness is not as safe as you initially thought it was. The GM makes a Move. \nEdges:\n'
+' - Attack from cover of darkness: You can attack an opponent unexpectedly, but reveal your position when you do.\n'
+' - Dive into the shadows: You disappear into the darkness.\n'
+' - Become one with the dark: You hide yourself so well nobody can find you. '
]



,'divinestrength' : [
'# Divine Strength'
,

' You can let your Higher Power imbue you with its strength. When you channel your Higher Power’s strength, you take +2 to Endure Injury and all your attacks are at +2 Harm for the scene’s duration. Until this divine power wears off, it manifests physically in your body; for example, your eyes turn all black, you radiate with a golden aura, or the shadows of wings appear on your back (the player describes). '
,

' You can let your Higher Power imbue you with its strength. When you channel your Higher Power’s strength, you take +2 to Endure Injury and all your attacks are at +2 Harm for the scene’s duration. Until this divine power wears off, it manifests physically in your body; for example, your eyes turn all black, you radiate with a golden aura, or the shadows of wings appear on your back (the player describes). '
,

' You can let your Higher Power imbue you with its strength. When you channel your Higher Power’s strength, you take +2 to Endure Injury and all your attacks are at +2 Harm for the scene’s duration. Until this divine power wears off, it manifests physically in your body; for example, your eyes turn all black, you radiate with a golden aura, or the shadows of wings appear on your back (the player describes). '
]



,'ethereal' : [
'# Ethereal'
,

' Choose 3 Edges. You may save up to 2 until later. \nEdges:\n'
+' - Ghostly movement: Move through a physical obstacle such as a person, wall, or door.\n'
+' - Weapons pass right through me: Completely avoid physical Harm.\n'
+' - Unrestrainable: Get out of a hold, bondage, or other physical objects trapping you. '
,

' Choose 2 Edges. You may save 1 until later. \nEdges:\n'
+' - Ghostly movement: Move through a physical obstacle such as a person, wall, or door.\n'
+' - Weapons pass right through me: Completely avoid physical Harm.\n'
+' - Unrestrainable: Get out of a hold, bondage, or other physical objects trapping you. '
,

' Choose 1 Edge but you attract spirits or other ethereal creatures. The GM makes a Move. \nEdges:\n'
+' - Ghostly movement: Move through a physical obstacle such as a person, wall, or door.\n'
+' - Weapons pass right through me: Completely avoid physical Harm.\n'
+' - Unrestrainable: Get out of a hold, bondage, or other physical objects trapping you. '
]



,'experienced' : [
'# Experienced'
,

' You have life experiences and skills from your life prior to becoming Enlightened. Choose any 1 Advantage from an Aware Archetype. '
,

' You have life experiences and skills from your life prior to becoming Enlightened. Choose any 1 Advantage from an Aware Archetype. '
,

' You have life experiences and skills from your life prior to becoming Enlightened. Choose any 1 Advantage from an Aware Archetype. '
]



,'immunity' : [
'# Immunity'
,

' You are immune to an elemental effect which is lethal to normal humans. When you are subjected to this element, only your clothes, gear, and other equipment suffer damage. Choose 1 option:\n'
+' - Fire.\n'
+' - Electricity.\n'
+' - Radioactivity.\n'
+' - Cold.\n'
+' - Chemicals (acids/poisons/drugs). '
,

' You are immune to an elemental effect which is lethal to normal humans. When you are subjected to this element, only your clothes, gear, and other equipment suffer damage. Choose 1 option:\n'
+' - Fire.\n'
+' - Electricity.\n'
+' - Radioactivity.\n'
+' - Cold.\n'
+' - Chemicals (acids/poisons/drugs). '
,

' You are immune to an elemental effect which is lethal to normal humans. When you are subjected to this element, only your clothes, gear, and other equipment suffer damage. Choose 1 option:\n'
+' - Fire.\n'
+' - Electricity.\n'
+' - Radioactivity.\n'
+' - Cold.\n'
+' - Chemicals (acids/poisons/drugs). '
]



,'improviser2' : [
'# Improviser2'
,

' You suffer no penalties to Perform a Ritual when outside your sanctum. '
,

' You suffer no penalties to Perform a Ritual when outside your sanctum. '
,

' You suffer no penalties to Perform a Ritual when outside your sanctum. '
]



,'initiate' : [
'# Initiate'
,

' You are an amateur who recently started experimenting with magic. '
,

' You are an amateur who recently started experimenting with magic. '
,

' You are an amateur who recently started experimenting with magic. '
]



,'invulnerability' : [
'# Invulnerability'
,

' You are invulnerable to a particular type of injury. When you are subjected to this type of injury, you get +3 to your Endure Injury roll. Choose 1 option:\n'
+' - Firearms.\n'
+' - Slicing and piercing weapons.\n'
+' - Bludgeoning weapons and crushing damage. '
,

' You are invulnerable to a particular type of injury. When you are subjected to this type of injury, you get +3 to your Endure Injury roll. Choose 1 option:\n'
+' - Firearms.\n'
+' - Slicing and piercing weapons.\n'
+' - Bludgeoning weapons and crushing damage. '
,

' You are invulnerable to a particular type of injury. When you are subjected to this type of injury, you get +3 to your Endure Injury roll. Choose 1 option:\n'
+' - Firearms.\n'
+' - Slicing and piercing weapons.\n'
+' - Bludgeoning weapons and crushing damage. '
]



,'journeyman' : [
'# Journeyman'
,

' (requires: Initiate) Your studies and experiments in your school of magic has granted you new insights. Chose 1 new Field of Expertise. \n\nJourneyman Ability: Protective Circle\n\n When you Perform a Ritual, you can choose this option:\n'
+' - You have protection from creatures and magical energies for as long as you remain within the protective circle. '
,

' (requires: Initiate) Your studies and experiments in your school of magic has granted you new insights. Chose 1 new Field of Expertise. \n\nJourneyman Ability: Protective Circle\n\n When you Perform a Ritual, you can choose this option:\n'
+' - You have protection from creatures and magical energies for as long as you remain within the protective circle. '
,

' (requires: Initiate) Your studies and experiments in your school of magic has granted you new insights. Chose 1 new Field of Expertise. \n\nJourneyman Ability: Protective Circle\n\n When you Perform a Ritual, you can choose this option:\n'
+' - You have protection from creatures and magical energies for as long as you remain within the protective circle. '
]



,'manipulatetheillusion' : [
'# Manipulate the Illusion'
,

' You permit the Illusion’s overwhelming force to cancel out the magic or rebuke the being. '
,

' You permit the Illusion’s overwhelming force to cancel out the magic or rebuke the being, but there are unexpected complications, such as the magic or being has time to affect you first, or your exertion of force attracts unwanted attention. '
,

' The Illusion temporarily rejects you. You may be overwhelmed, transported elsewhere, or become the target of beings who now see you clearly. The GM makes a Move. '
]



,'master' : [
'# Master'
,

' (requires: Adept) You are one of the few people alive with magical abilities akin to beings from the supernatural realms. Choose 1 new Field of Expertise. Additionally, you may always choose 1 additional effect when you Perform a Ritual. '
,

' (requires: Adept) You are one of the few people alive with magical abilities akin to beings from the supernatural realms. Choose 1 new Field of Expertise. Additionally, you may always choose 1 additional effect when you Perform a Ritual. '
,

' (requires: Adept) You are one of the few people alive with magical abilities akin to beings from the supernatural realms. Choose 1 new Field of Expertise. Additionally, you may always choose 1 additional effect when you Perform a Ritual. '
]



,'masterofrites' : [
'# Master of Rites'
,

' Choose up to 2 options anytime during the following scene. \nOptions:\n'
+' - Imbue a group of human NPCs (consenting or not) with your Higher Power’s Principle. They are now your followers.\n'
+' - Enslave a person present to the Principles of your Higher Power. An NPC is bound to act in accordance with this Principle. A PC who fails to Keep it Together becomes bound to it, and gains +1 Stability when acting in accordance with the Principle, and −1 Stability when acting in opposition to it. A PC can break this mental bondage by using magic tied to the Higher Power’s domain, or by killing The Disciple.\n'
+' - Spread your Higher Power’s influence in the local society. Take +2 next time you use a suitable Ability in a way connected to your Higher Power.\n'
+' - Summon your Higher Power and ask it for something. It can reveal itself to you through visions, incarnations, or through its priesthood (be it angels or nepharites). The GM determines if you can have what you are requesting and, if so, what is required of you in return. '
,

' Choose 1 option anytime during the following scene. \nOptions:\n'
+' - Imbue a group of human NPCs (consenting or not) with your Higher Power’s Principle. They are now your followers.\n'
+' - Enslave a person present to the Principles of your Higher Power. An NPC is bound to act in accordance with this Principle. A PC who fails to Keep it Together becomes bound to it, and gains +1 Stability when acting in accordance with the Principle, and −1 Stability when acting in opposition to it. A PC can break this mental bondage by using magic tied to the Higher Power’s domain, or by killing The Disciple.\n'
+' - Spread your Higher Power’s influence in the local society. Take +2 next time you use a suitable Ability in a way connected to your Higher Power.\n'
+' - Summon your Higher Power and ask it for something. It can reveal itself to you through visions, incarnations, or through its priesthood (be it angels or nepharites). The GM determines if you can have what you are requesting and, if so, what is required of you in return. '
,

' The ritual failed for whatever reason. The GM makes a Move. '
]



,'memoriesofpastlives' : [
'# Memories of Past Lives'
,

' Choose any 1 Advantage from an Aware Archetype. '
,

' Choose any 1 Advantage from an Aware Archetype. '
,

' Choose any 1 Advantage from an Aware Archetype. '
]



,'mindmanipulator' : [
'# Mind Manipulator'
,

' Choose up to 3 options. \nOptions:\n'
+' - Search their memories for a specific event. You experience this memory as if it was your own.\n'
+' - Ask the person what their surface thoughts are at the moment.\n'
+' - Search for specific information the person should know.\n'
+' - Plant a false memory. It will fade and disappear within a few hours, but will feel real until then. '
,

' Choose up to 2 options. \nOptions:\n'
+' - Search their memories for a specific event. You experience this memory as if it was your own.\n'
+' - Ask the person what their surface thoughts are at the moment.\n'
+' - Search for specific information the person should know.\n'
+' - Plant a false memory. It will fade and disappear within a few hours, but will feel real until then. '
,

' Choose 1 option, but you also open your mind to the person you’re reading. They pick one option to use against you as well. \nOptions:\n'
+' - Search their memories for a specific event. You experience this memory as if it was your own.\n'
+' - Ask the person what their surface thoughts are at the moment.\n'
+' - Search for specific information the person should know.\n'
+' - Plant a false memory. It will fade and disappear within a few hours, but will feel real until then. '
]



,'naturalweapons' : [
'# Natural Weapons'
,

' Your body incorporates natural weaponry. These can include claws, fangs, tentacles, horns, armored limbs, or technological alterations, such as integrated knife blades. When you Engage in (close) Combat using your natural weapons, you deal 3 Harm. '
,

' Your body incorporates natural weaponry. These can include claws, fangs, tentacles, horns, armored limbs, or technological alterations, such as integrated knife blades. When you Engage in (close) Combat using your natural weapons, you deal 3 Harm. '
,

' Your body incorporates natural weaponry. These can include claws, fangs, tentacles, horns, armored limbs, or technological alterations, such as integrated knife blades. When you Engage in (close) Combat using your natural weapons, you deal 3 Harm. '
]



,'openerofways' : [
'# Opener of Ways'
,

' The portal is stable and remains so throughout the scene or until you close it. If you venture through the portal, you are able to reconstruct it leading back to the same location at will. '
,

' The portal remains open for only a few minutes, after which it seals shut. If you venture through the portal, you must open a new one to return. '
,

' The portal is unstable; it can close at any time, lead to an undetermined location, interfere with the Illusion, or attract the guardians of the Illusion. The GM makes a Move. '
]



,'quick' : [
'# Quick'
,

' Choose 3 Edges. You may save up to 2 until later. \nEdges:\n'
+' - Immediate interrupt: Act before someone else completes their action.\n'
+' - Blur of motion: Instantly transport yourself between two range increments before anyone can react; for example, moving from field to room, or from room to arm.\n'
+' - Attack with the speed of lightning: Engage someone in (close) combat so rapidly they do not get a chance to Avoid Harm.\n'
+' - Flurry of blows: Engage in combat with one additional target, over and above the number of targets the attack normally allows. '
,

' Choose 2 Edges. You may save 1 until later. \nEdges:\n'
+' - Immediate interrupt: Act before someone else completes their action.\n'
+' - Blur of motion: Instantly transport yourself between two range increments before anyone can react; for example, moving from field to room, or from room to arm.\n'
+' - Attack with the speed of lightning: Engage someone in (close) combat so rapidly they do not get a chance to Avoid Harm.\n'
+' - Flurry of blows: Engage in combat with one additional target, over and above the number of targets the attack normally allows. '
,

' Choose 1 Edge, but you attract unwanted complications. The GM makes a Move. \nEdges:\n'
+' - Immediate interrupt: Act before someone else completes their action.\n'
+' - Blur of motion: Instantly transport yourself between two range increments before anyone can react; for example, moving from field to room, or from room to arm.\n'
+' - Attack with the speed of lightning: Engage someone in (close) combat so rapidly they do not get a chance to Avoid Harm.\n'
+' - Flurry of blows: Engage in combat with one additional target, over and above the number of targets the attack normally allows. '
]



,'regenerate' : [
'# Regenerate'
,

' Your body heals unnaturally fast. Serious wounds vanish completely in a few hours and critical wounds heal within a day. However, severe injuries may leave ugly scars and misshapen tissue. '
,

' Your body heals unnaturally fast. Serious wounds vanish completely in a few hours and critical wounds heal within a day. However, severe injuries may leave ugly scars and misshapen tissue. '
,

' Your body heals unnaturally fast. Serious wounds vanish completely in a few hours and critical wounds heal within a day. However, severe injuries may leave ugly scars and misshapen tissue. '
]



,'summoner' : [
'# Summoner'
,

' You summon the creature(s), who will obey your orders for one day. '
,

' You summon the creature(s), who will either obey your orders for one scene or fulfill a single order that takes longer. You do not have full control over the creature(s), who will act on their own accord and interpret your orders as they wish. '
,

' You summon the creature(s), who are not under your power at all, but act according to their own whims. '
]



,'talisman' : [
'# Talisman'
,

' Choose 3 options. Options\n'
+' - Find a particular place in the realm of Death.\n'
+' - Find a portal back to the lands of the living.\n'
+' - Steel your senses against the influences of the realm of Death or the magic of its inhabitants. '
,

' Choose 1 option. Options\n'
+' - Find a particular place in the realm of Death.\n'
+' - Find a portal back to the lands of the living.\n'
+' - Steel your senses against the influences of the realm of Death or the magic of its inhabitants. '
,

' The talisman fails you. The GM makes a Move. '
]



,'telekinesis' : [
'# Telekinesis'
,

' You can move objects using the power of your mind, but the larger they are, the more mental effort is required. When you use telekinesis as a weapon, you can perform the following attacks:\n'
+' - Launch a small object [1] [Distance: room, e.g., glass, vase, bottle].\n'
+' - Launch a medium-sized object [2] [Distance: room, decreases Stability by –1, e.g., television, table, armchair].\n'
+' - Launch a large object [3] [Distance: room, decreases Stability by –2, e.g., car, shipping container]. '
,

' You can move objects using the power of your mind, but the larger they are, the more mental effort is required. When you use telekinesis as a weapon, you can perform the following attacks:\n'
+' - Launch a small object [1] [Distance: room, e.g., glass, vase, bottle].\n'
+' - Launch a medium-sized object [2] [Distance: room, decreases Stability by –1, e.g., television, table, armchair].\n'
+' - Launch a large object [3] [Distance: room, decreases Stability by –2, e.g., car, shipping container]. '
,

' You can move objects using the power of your mind, but the larger they are, the more mental effort is required. When you use telekinesis as a weapon, you can perform the following attacks:\n'
+' - Launch a small object [1] [Distance: room, e.g., glass, vase, bottle].\n'
+' - Launch a medium-sized object [2] [Distance: room, decreases Stability by –1, e.g., television, table, armchair].\n'
+' - Launch a large object [3] [Distance: room, decreases Stability by –2, e.g., car, shipping container]. '
]



,'templars' : [
'# Templars'
,

' If carrying out the mission is reasonably with the realm of their capability, they perform their tasks flawlessly and exactly as instructed. '
,

' The mission suffers some kind of complication. Maybe it works out okay but has unexpected fallout afterwards, or things didn’t work out as you intended. '
,

' Something goes wrong. Maybe the mission isn’t completed according to directions, serious problems arise as a consequence, or some or all of the templars are injured, captured, or killed. '
]



,'unnaturallystrong' : [
'# Unnaturally Strong'
,

' You are extremely strong. Actions like bending iron bars, bashing in doors, or lifting hundreds of kilograms are not a problem for you. You take +1 Harm to all close combat attacks, and once you have locked someone during unarmed combat, you can choose this attack option:\n'
+' - Crush [4] [Distance: arm, victim must already be locked]. You are also capable of lifting and throwing heavy objects as a ranged attack:\n'
+' - Throw heavy object [3] [Distance: room]. '
,

' You are extremely strong. Actions like bending iron bars, bashing in doors, or lifting hundreds of kilograms are not a problem for you. You take +1 Harm to all close combat attacks, and once you have locked someone during unarmed combat, you can choose this attack option:\n'
+' - Crush [4] [Distance: arm, victim must already be locked]. You are also capable of lifting and throwing heavy objects as a ranged attack:\n'
+' - Throw heavy object [3] [Distance: room]. '
,

' You are extremely strong. Actions like bending iron bars, bashing in doors, or lifting hundreds of kilograms are not a problem for you. You take +1 Harm to all close combat attacks, and once you have locked someone during unarmed combat, you can choose this attack option:\n'
+' - Crush [4] [Distance: arm, victim must already be locked]. You are also capable of lifting and throwing heavy objects as a ranged attack:\n'
+' - Throw heavy object [3] [Distance: room]. '
]



,'unyielding' : [
'# Unyielding'
,

' By steeling yourself and lowering Stability by –1, you take +2 to all rolls to Keep it Together whenever you resist magical influence during this scene. '
,

' By steeling yourself and lowering Stability by –1, you take +2 to all rolls to Keep it Together whenever you resist magical influence during this scene. '
,

' By steeling yourself and lowering Stability by –1, you take +2 to all rolls to Keep it Together whenever you resist magical influence during this scene. '
]



,'branded' : [
'# Branded'
,

' You avoid the pursuing entities. '
,

' An entity has latched onto you. The GM takes 1 Hold. The GM can spend a Hold to make a Move for the entities. An entity might possess someone close to the character, reveal itself to them, challenge them, or stalk them. A portal might open to the Deathrealm. One or several entities may try to trick or lure them into the Death realm, or a malevolent being gains possession of them. '
,

' Several entities, or one very powerful death-being, is on your trail. The GM takes 3 Hold. The GM can spend a Hold to make a Move for the entities. An entity might possess someone close to the character, reveal itself to them, challenge them, or stalk them. A portal might open to the Deathrealm. One or several entities may try to trick or lure them into the Death realm, or a malevolent being gains possession of them. '
]



,'creator' : [
'# Creator'
,

' You are safe from your creator. '
,

' Your creator catches your scent. The GM takes 1 Hold. The GM can spend a Hold to make a Move for your creator. For example, your creator might send henchmen or other experiments to bring you back, target someone you care about, gives you an order and expects you to follow through, or provides you with unexpected insights into your origin or purpose. '
,

' You have revealed yourself to your creator. The GM takes 3 Hold. The GM can spend a Hold to make a Move for your creator. For example, your creator might send henchmen or other experiments to bring you back, target someone you care about, gives you an order and expects you to follow through, or provides you with unexpected insights into your origin or purpose. '
]



,'persecutors' : [
'# Persecutors'
,

' You are safe from your persecutors, for the moment. '
,

' You’ve left a trail for your persecutors to follow. The GM takes 1 Hold. The GM can spend a Hold to make a Move for your persecutors. They might set up a trap, track down your hideout, infiltrate your environment, capture one of your allies, steal or destroy something you own, appear unexpectedly, or make common cause with one of your other enemies. '
,

' Your persecutors have tracked you down. The GM takes 3 Hold. The GM can spend a Hold to make a Move for your persecutors. They might set up a trap, track down your hideout, infiltrate your environment, capture one of your allies, steal or destroy something you own, appear unexpectedly, or make common cause with one of your other enemies. '
]



,'protege' : [
'# Protege'
,

' Nothing happens. '
,

' Your protégé makes an appearance. The GM takes 1 Hold. The GM can spend a Hold to make a Move for your protégé. For example, someone extorts you by threatening to harm your protégé, or your protégé might return to ask for your help, sabotage one of your plans, (threaten to) reveal one of your secrets, steal something of yours, or slander you. '
,

' Your protégé puts you in a difficult spot. The GM takes 3 Hold. The GM can spend a Hold to make a Move for your protégé. For example, someone extorts you by threatening to harm your protégé, or your protégé might return to ask for your help, sabotage one of your plans, (threaten to) reveal one of your secrets, steal something of yours, or slander you. '
]



,'bloodthirst' : [
'# Bloodthirst'
,

' You must drink human blood to survive. If you haven’t drunk the equivalent of one adult’s or three children’s blood supply within two week’s time, you suffer a Critical Wound from withering away, which can only be healed by drinking the blood you require – if not more. If you go an additional week without sustenance, you end up in a coma. The week after that, you die, unless someone feeds you human blood. To drink blood without causing 2 Harm is an Act Under Pressure. '
,

' You must drink human blood to survive. If you haven’t drunk the equivalent of one adult’s or three children’s blood supply within two week’s time, you suffer a Critical Wound from withering away, which can only be healed by drinking the blood you require – if not more. If you go an additional week without sustenance, you end up in a coma. The week after that, you die, unless someone feeds you human blood. To drink blood without causing 2 Harm is an Act Under Pressure. '
,

' You must drink human blood to survive. If you haven’t drunk the equivalent of one adult’s or three children’s blood supply within two week’s time, you suffer a Critical Wound from withering away, which can only be healed by drinking the blood you require – if not more. If you go an additional week without sustenance, you end up in a coma. The week after that, you die, unless someone feeds you human blood. To drink blood without causing 2 Harm is an Act Under Pressure. '
]



,'boundtohigherpower' : [
'# Bound to Higher Power'
,

' You receive a vision of your Higher Power admonishing you, but letting you off with a warning. '
,

' You have a vision of your Higher Power demanding penance for your sins. Should you refuse this penance, the Higher Power punishes you as if you rolled a –9. Penance options include (GM’s choice):\n'
+' - You must select and offer up a living sacrifice to your Higher Power. The sacrifice should be one of the Higher Power’s enemies, one of your followers, or someone you care about. The victim is forced to serve the Higher Power for life, or have their life ended.\n'
+' - You must accomplish something that strengthens the Higher Power’s Principle, GM’s choice of what.\n'
+' - You must be tested in a trial to prove your devotion to the Higher Power. It is the GM’s choice how, but it should be dangerous. '
,

' Your Higher Power punishes you. The GM chooses 1 option:\n'
+' - The Higher Power demands a blood sacrifice of their own choosing.\n'
+' - The Higher Power marks you, so all can bear witness to your sins (e.g., stigmata, misshapen body part, rotting flesh, a symbol branded onto your face, unnatural eyes, or hairlessness).\n'
+' - The Higher Power gives you a mission and withdraws the Abilities it conferred upon you until you have completed it. '
]



,'cannibalism' : [
'# Cannibalism'
,

' You must consume human flesh in order to survive. If you haven’t eaten the equivalent of one adult or three children within two week’s time, you suffer a Critical Wound from decomposition, which can only be healed by eating the flesh you require – if not more. If you go an additional week without sustenance, you end up in a coma. The week after that, you die, unless someone feeds you human flesh. '
,

' You must consume human flesh in order to survive. If you haven’t eaten the equivalent of one adult or three children within two week’s time, you suffer a Critical Wound from decomposition, which can only be healed by eating the flesh you require – if not more. If you go an additional week without sustenance, you end up in a coma. The week after that, you die, unless someone feeds you human flesh. '
,

' You must consume human flesh in order to survive. If you haven’t eaten the equivalent of one adult or three children within two week’s time, you suffer a Critical Wound from decomposition, which can only be healed by eating the flesh you require – if not more. If you go an additional week without sustenance, you end up in a coma. The week after that, you die, unless someone feeds you human flesh. '
]



,'controlledbyexternalforce' : [
'# Controlled by External Force'
,

' You have made a pact with a demon or Higher Power (see Chapter 21 – Pacts and Magic). It could be a nepharite, an angel, a forgotten god, or even an Archon or a Death Angel. If the pact is broken in any way, you could lose your powers, become human again, or be obliterated '
,

' You have made a pact with a demon or Higher Power (see Chapter 21 – Pacts and Magic). It could be a nepharite, an angel, a forgotten god, or even an Archon or a Death Angel. If the pact is broken in any way, you could lose your powers, become human again, or be obliterated '
,

' You have made a pact with a demon or Higher Power (see Chapter 21 – Pacts and Magic). It could be a nepharite, an angel, a forgotten god, or even an Archon or a Death Angel. If the pact is broken in any way, you could lose your powers, become human again, or be obliterated '
]



,'fieldofexpertise' : [
'# Field of Expertise'
,

' Field of expertise denotes what aspects of Death magic the magician has insight into. Whenever the Death Magician Performs a Ritual in a field she’s not familiar with, she may not choose the option “the ritual doesn’t become unstable.” At character creation, choose 1 Field of Expertise for your Death Magician:\n'
+' - Communicate with the dead.\n'
+' - Open portals to Inferno.\n'
+' - Summoning.\n'
+' - Affect the living.\n'
+' - Bind and exorcise. '
,

' Field of expertise denotes what aspects of Death magic the magician has insight into. Whenever the Death Magician Performs a Ritual in a field she’s not familiar with, she may not choose the option “the ritual doesn’t become unstable.” At character creation, choose 1 Field of Expertise for your Death Magician:\n'
+' - Communicate with the dead.\n'
+' - Open portals to Inferno.\n'
+' - Summoning.\n'
+' - Affect the living.\n'
+' - Bind and exorcise. '
,

' Field of expertise denotes what aspects of Death magic the magician has insight into. Whenever the Death Magician Performs a Ritual in a field she’s not familiar with, she may not choose the option “the ritual doesn’t become unstable.” At character creation, choose 1 Field of Expertise for your Death Magician:\n'
+' - Communicate with the dead.\n'
+' - Open portals to Inferno.\n'
+' - Summoning.\n'
+' - Affect the living.\n'
+' - Bind and exorcise. '
]



,'huntinginstincts' : [
'# Hunting Instincts'
,

' You keep your Hunting Instincts at bay. '
,

' If you choose to resist hunting your prey, it will mentally drain you. Stability −1. '
,

' You must have your prey now. If you cannot, you start feeling terrible. Stability −4. '
]



,'inhumanappearance' : [
'# Inhuman Appearance'
,

' You look entirely inhuman and must wear a disguise to be able to exist around others. For example, your skin might be rotting and peeling off, your body parts are misshapen, your limbs are warped, mechanical objects have been integrated underneath your skin, or you have features of insects or spiders. When humans perceive your true appearance, they are overcome by disgust, fear, and panic. '
,

' You look entirely inhuman and must wear a disguise to be able to exist around others. For example, your skin might be rotting and peeling off, your body parts are misshapen, your limbs are warped, mechanical objects have been integrated underneath your skin, or you have features of insects or spiders. When humans perceive your true appearance, they are overcome by disgust, fear, and panic. '
,

' You look entirely inhuman and must wear a disguise to be able to exist around others. For example, your skin might be rotting and peeling off, your body parts are misshapen, your limbs are warped, mechanical objects have been integrated underneath your skin, or you have features of insects or spiders. When humans perceive your true appearance, they are overcome by disgust, fear, and panic. '
]



,'sensitivity' : [
'# Sensitivity'
,

' You’re particularly sensitive to something. You don’t enjoy being in the vicinity of the element, and if you take Harm involving your sensitivity, you receive an additional +2 Harm. Choose 1 option:\n'
+' - Fire.\n'
+' - Electricity.\n'
+' - Iron (not steel).\n'
+' - Silver.\n'
+' - Sunlight (take 2 Harm when exposed to direct sunlight on bare skin).\n'
+' - Water (take 2 Harm when exposed to water on your bare skin).\n'
+' - Wood. '
,

' You’re particularly sensitive to something. You don’t enjoy being in the vicinity of the element, and if you take Harm involving your sensitivity, you receive an additional +2 Harm. Choose 1 option:\n'
+' - Fire.\n'
+' - Electricity.\n'
+' - Iron (not steel).\n'
+' - Silver.\n'
+' - Sunlight (take 2 Harm when exposed to direct sunlight on bare skin).\n'
+' - Water (take 2 Harm when exposed to water on your bare skin).\n'
+' - Wood. '
,

' You’re particularly sensitive to something. You don’t enjoy being in the vicinity of the element, and if you take Harm involving your sensitivity, you receive an additional +2 Harm. Choose 1 option:\n'
+' - Fire.\n'
+' - Electricity.\n'
+' - Iron (not steel).\n'
+' - Silver.\n'
+' - Sunlight (take 2 Harm when exposed to direct sunlight on bare skin).\n'
+' - Water (take 2 Harm when exposed to water on your bare skin).\n'
+' - Wood. '
]



,'soulthirst' : [
'# Soul Thirst'
,

' You must feed on people’s life force to survive. The drinking from a person’s soul usually occurs during sex, or by kissing/ touching a sleeping or unconscious person. In order to survive, you must devour the equivalency of one human soul per week (10 Stability points). It could consist of one victim who you devour entirely – leaving an apathetic husk in your wake – or several victims, who are all tapped of a bit of their life force. Anyone subjected to the Soul Thirst without being devoured gradually loses their life force, becoming pale and depressed (−1 to −9 Stability). When the victim’s Stability reaches 0 (Broken), you devour the final remnants of her soul. If you fail to devour the equivalency of one human soul each week, you lose an amount of Stability equal to that which you lacked (i.e., if you lack 3 Stability ‘feeding’ points by week’s end, you lose 3 Stability). If your Stability reaches 0 due to this, you become an ethereal phantom until you once again gain the chance to devour human souls. '
,

' You must feed on people’s life force to survive. The drinking from a person’s soul usually occurs during sex, or by kissing/ touching a sleeping or unconscious person. In order to survive, you must devour the equivalency of one human soul per week (10 Stability points). It could consist of one victim who you devour entirely – leaving an apathetic husk in your wake – or several victims, who are all tapped of a bit of their life force. Anyone subjected to the Soul Thirst without being devoured gradually loses their life force, becoming pale and depressed (−1 to −9 Stability). When the victim’s Stability reaches 0 (Broken), you devour the final remnants of her soul. If you fail to devour the equivalency of one human soul each week, you lose an amount of Stability equal to that which you lacked (i.e., if you lack 3 Stability ‘feeding’ points by week’s end, you lose 3 Stability). If your Stability reaches 0 due to this, you become an ethereal phantom until you once again gain the chance to devour human souls. '
,

' You must feed on people’s life force to survive. The drinking from a person’s soul usually occurs during sex, or by kissing/ touching a sleeping or unconscious person. In order to survive, you must devour the equivalency of one human soul per week (10 Stability points). It could consist of one victim who you devour entirely – leaving an apathetic husk in your wake – or several victims, who are all tapped of a bit of their life force. Anyone subjected to the Soul Thirst without being devoured gradually loses their life force, becoming pale and depressed (−1 to −9 Stability). When the victim’s Stability reaches 0 (Broken), you devour the final remnants of her soul. If you fail to devour the equivalency of one human soul each week, you lose an amount of Stability equal to that which you lacked (i.e., if you lack 3 Stability ‘feeding’ points by week’s end, you lose 3 Stability). If your Stability reaches 0 due to this, you become an ethereal phantom until you once again gain the chance to devour human souls. '
]



,'symbolbondage' : [
'# Symbol Bondage'
,

' You are bound to a symbol. It could be anything from a piece of jewelry to a building or a tattoo on someone else’s body. Whenever the symbol is harmed, you suffer sympathetic injuries. If the symbol is destroyed, you are also obliterated. For as long as the symbol remains intact, you cannot truly die; rising from the grave, if you do. However, if someone discovers the symbol, they can gain power over you – even summon you to them to do their bidding. Furthermore, for as long as they possess the symbol, you cannot harm them. '
,

' You are bound to a symbol. It could be anything from a piece of jewelry to a building or a tattoo on someone else’s body. Whenever the symbol is harmed, you suffer sympathetic injuries. If the symbol is destroyed, you are also obliterated. For as long as the symbol remains intact, you cannot truly die; rising from the grave, if you do. However, if someone discovers the symbol, they can gain power over you – even summon you to them to do their bidding. Furthermore, for as long as they possess the symbol, you cannot harm them. '
,

' You are bound to a symbol. It could be anything from a piece of jewelry to a building or a tattoo on someone else’s body. Whenever the symbol is harmed, you suffer sympathetic injuries. If the symbol is destroyed, you are also obliterated. For as long as the symbol remains intact, you cannot truly die; rising from the grave, if you do. However, if someone discovers the symbol, they can gain power over you – even summon you to them to do their bidding. Furthermore, for as long as they possess the symbol, you cannot harm them. '
]



,'uncontrolledshapeshifting' : [
'# Uncontrolled Shapeshifting'
,

' You retain your human form. '
,

' You gain some inhuman features. '
,

' You are contorted into something entirely inhuman. The GM takes control of your character until it wears off, at most one full scene after your transformation.'
]
















}



