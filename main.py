import random
from feats import *

input('''Welcome to my text-based adventure game.\n
----------------------------------\n
This game requires use of the number keys to make choices,\n
and the enter key to submit or to advance.\n
(press enter to continue)\n''')

# explanation of stats

input('''\nThis game uses 4 primary stats:\n
STR - Strength, how much damage you deal with attacks\n
SPD - Speed, how nimble and dexterous you are\n
FOC - Focus, your ability to focus and stay calm in dangerous situations\n
RES - Resilience, how much damage you can take before falling\n
(press enter to continue)\n''')

input('''\nThese feed into 4 secondary stats:\n
PHYS - Physique, how physically strong you are. Equal to STR + SPD\n
REFL - Reflex, how quickly you can react to events. Equal to SPD + FOC\n
WILL - Willpower, how well your character can deal with hardships. Equal to FOC + RES\n
CONS - Constitution, how healthy you are. Equal to RES + STR\n
(press enter to continue)\n''')

# optional plot

verif_Success = False
while not verif_Success:
    verif = input('''\nWould you like to learn the story of this game?
1) Yes     2) No\n''')
    try:
        if int(verif) not in [1,2]:
            raise indexError
        
        else:
            if int(verif) == 1:
                verif_Success = True
                story = True
            elif int(verif) == 2:
                verif_Success = True
                story = False

    except:
        print('Please choose 1 or 2')

if story:
    input('\nAround a century ago, a tree was born which had magical powers. The tree\'s powers grew stronger with it, and eventually the tree started spreading its magic to its surroundings, birthing the magical Sylphes Forest.\n')
    input('The forest drew many researchers towards it, and the researchers set up outposts in and around the forest. Eventually, more people became interested in the forest and quickly the snall outposts grew to large towns and villages.\n')
    input('Your grandparents were among the people who first moved to the towns surrounding the forest, and now you live there with your parents.\n')
    input('But recently, something strange has twisted the tree\'s magic, corrupting it and the forest. People and animals were turned into monsters, and several hundreds died in the aftermath of the weird event.')
    input('Your parents were among those killed, but you were able to escape. Now, after several years of training, you set off towards the village of Arbolyn, situated near the center of the forest, to try to find what turned the magic evil, and put a stop to it.')

# optional tutorial

verif_Success = False
while not verif_Success:
    verif = input('''\nWould you like to see a tutorial?
1) Yes     2) No\n''')
    try:
        if int(verif) not in [1,2]:
            raise indexError
        
        else:
            if int(verif) == 1:
                verif_Success = True
                tutorial = True
            elif int(verif) == 2:
                verif_Success = True
                tutorial = False

    except:
        print('Please choose 1 or 2')

if tutorial:
    input('''\nWhile exploring and during combat, your exhaustion level increases. When your exhaustion reaches 90 + FOC, you faint, instantly losing combat and returning to the village. While out of combat, you can rest to remove part of your exhaustion at a cost.
Combat in this game is turn based. Turn order is decided by who has the higher SPD stat.
You have health equal to 10 + 3* your RES stat. When you take damage, your health is reduced by the total. If your health reaches zero, you lose the fight. If you faint to exhaustion during combat, you also instantly lose the fight.''')

    input('''\nDuring your turn in combat, you have several actions available to you.
Using an item will allow you to choose an item in your inventory to activate its effect. Unless stated otherwise, items are one-use and will delete themselves after being used.
Escaping will allow you to make an attempt to escape. To escape, you must roll a d20 and add SPD. If the total is higher than the enemy's REFL, you successfully escape. Attempting an escape increases your exhaustion. Successfully escaping will instantly end the combat, counting as neither a win nor a defeat. If you escape, you will gain reduced EXP based on the enemy's remaining health.''')

    input('''\nWhen a character attacks a target, the attacker's PHYS is added to a counter, called the target's attack counter. When a character's attack counter reaches 3 * their CONS, the counter is reduced and they are hit by the attack and dealt damage. The base damage dealt is equal to the attacker's STR, but weapons add to that, as do certain feats
It is important to know that while damage and effects from being hit can be random, the act of being hit is not random. You should keep in mind your attack counter and your enemy's when evaluating what action to take on your turns. ''')

    input('''\nWinning combat will reward you with EXP and items. When your total EXP points reach certain thresholds, you level up and gain a stat point, which you can use to increase your stats.
Losing combat will send you back to the village with no rewards, and will increase a stat called corruption.
Corruption symbolises how much the forest\'s magic has affected you. Corruption slightly decreases your FOC and RES, as well as having other effects, so the more corrupt you are the easier it is to gain corruption, and the harder it becomes to stop yourself from gaining it.
Corruption can also have effects on events that happen to you in the village.''')

    input('''\nCorruption can also be gained from events and while resting in the forest. Corruption gained from outside of combat can be reduced or even completely negated based on your WILL stat.
Reaching 100 corruption ends the game.
However, gaining corruption also gives you feat points, which you can use to unlock or upgrade feats in the village.
You should always evaluate the risk vs reward of gaining corruption.''')

    
# import character classes and stats from file, as well as items and dice

from dice import *
import items

import characters

#character select

select_Success = False

charlist = characters.charlist()

while not select_Success:
    print('\nSelect your character:')
    num = 1
    for char in charlist:
        print(f'\n{num}) {char["name"].name} ({char["name"].pronouns["pers"]}/{char["name"].pronouns["obj"]})'.ljust(23, ' ') + f'Strengths: {", ".join(char["strengths"]).upper()}    Weakness: {char["weakness"].upper()}')
        num += 1

    charc = input()


    try:
        if int(charc) not in range(1, num):
            raise indexError
        else:
            select2_Success = False

            while not select2_Success:

                selected = characters.charvars[int(charc) -1]

                verif = input(f'''\n{selected.name}:\n
STR: {selected.str} {"".ljust(selected.str,"■")}
SPD: {selected.spd} {"".ljust(selected.spd,"■")}
FOC: {selected.foc} {"".ljust(selected.foc,"■")}
RES: {selected.res} {"".ljust(selected.res,"■")}

Starting feat: {selected.feat.name}
{selected.feat.description}

Select {selected.name}?
1) Yes     2) No\n''')
                
                
                try:
                    if int(verif) not in [1,2]:
                        raise indexError
                    
                    else:
                        if int(verif) == 1:
                            charc = selected
                            select_Success = True
                            select2_Success = True
                        elif int(verif) == 2:
                            select2_Success = True

                except:
                    print('Please choose 1 or 2')
                    
                
    except:
        print('Please choose 1, 2, 3, or 4')

print(f'\nYou are playing as {charc.name}\n\n\n\n\n')

# setting up combat stats



maxHP = 10 + charc.res * 3
currentHP = maxHP
atkCounterMax = charc.cons * 3
corruption = 0
exhaustion = 0
corruptionPenalty = max(0, 2**((corruption + 70)/140) - 1.45)

level = 1
exp = [0, ((level + 9)**3)/10]

equip = ['Old Sword']
equipMax = 1

inventory = ['Old Sword']

#unicode characters

slash = u"\u0336"

#defining function for taking weapon from inventory and equiping it

def equip(name, replace = equip[0]):
    if len(equipMax) > len(equip):
        equip.append(name)

    else:
        pass


# num of expores until player arrives at village

villageDistance = 3


while villageDistance:

    if villageDistance == 3:
        print(f'''\nAfter many days of traveling, {charc.name} has finally arrived at the Sylphes Forest.\n
\n{charc.name}: Just a bit longer and the village will be in sight!\n''')

    elif villageDistance == 2:
        pass

    else:
        pass
    
    choice = input(f'''Distance to village : {villageDistance}\n
Exhaustion: {exhaustion}
Current Health: {currentHP} / {maxHP}

1) keep exploring\n
2) inventory\n
3) stats\n
4) {"".join(["{}{}".format(slash,c) for c in "rest"]) + "(requires 50+ exhaustion)" if exhaustion < 50 else "rest"}''')

    try:
        if int(choice) == 4 and exhaustion >= 50:
            pass
            
        if int(choice) == 3:
            pass

        elif int(choice) == 2:
            itemCount = 0
            pageCount = 0
            printList = []
            for i in inventory:
                itemCount += 1
                pageCount += 1
                item = items.iSeek(i)
                string = f'{pageCount}) {item.name} - {item.effects}'
                printList.append(string)
                if pageCount == 5:
                    pageCount = 0
            page = 1
            while True:
                print(f'\nInventory ({itemCount} items):\nPage {page} of {(itemCount - 1)//5 + 1}\n')
                print('\n'.join(printList[5*(page - 1) : min(itemCount, 5*page)]) + '\n')
                if itemCount > 5 * page:
                    print('\n7) Next page')
                if page > 1:
                    print('\n8) Previous page')
                choice = input('''\n9) Go back\n
Choose an item to get more information about it.\n''')

                
                try:
                    if int(choice) + 5*(page - 1) in range(5*(page - 1), min(itemCount, 5*page) + 1):
                        item = items.iSeek(inventory[5*page + int(choice) - 6])
                        input(f'''\n{item.name}:
{item.description}
{item.effects}

Value: {item.value}\n''')
                    elif int(choice) == 7 and itemCount > 5 * page:
                        page += 1
                    elif int(choice) == 8 and page > 1:
                        page -= 1
                    elif int(choice) == 9:
                        break
                    else:
                        raise indexError
                    
                except:
                    print('Please choose a valid option\n')
                
        elif int(choice) == 1:
            input('Kay explores deeper into the forest. +5 exhaustion')
            exhaustion += 5

            print('A Bear jumps out of the foliage!')
            

            enemy = BearStarter

            while True:
                pass
        else:
            raise indexError
    except:
        print('Please choose a valid option\n')
