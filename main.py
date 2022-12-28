import random

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

# optional tutorial

verif_Success = False
while not verif_Success:
    verif = input('''\nWould you like to see an explanation of combat?
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
    input('''tutorial
''')

# import character classes and stats from file

import characters
from characters import Character



#character select

select_Success = False

charlist = characters.charlist()

while not select_Success:
    print('\nSelect your character:')
    num = 1
    for char in charlist:
        print('\n{}) {} ({}/{})'.format(num, char['name'].name, char['name'].pronouns['pers'], char['name'].pronouns['obj']).ljust(23, ' ') + 'Strengths: {}    Weakness: {}'.format(', '.join(char['strengths']).upper(), char['weakness'].upper()))
        num += 1

    charc = input()


    try:
        if int(charc) not in range(1, num):
            raise indexError
        else:
            select2_Success = False

            while not select2_Success:

                selected = characters.charvars[int(charc) -1]

                verif = input('''\n{}:\n
STR: {} {}
SPD: {} {}
FOC: {} {}
RES: {} {}

Select {}?
1) Yes     2) No\n'''.format(selected.name,
                             selected.str, ''.ljust(selected.str,'■'),
                             selected.spd, ''.ljust(selected.spd,'■'),
                             selected.foc, ''.ljust(selected.foc,'■'),
                             selected.res, ''.ljust(selected.res,'■'),
                             selected.name))
                
                
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

print('\nYou are playing as {}\n\n\n\n\n'.format(charc.name))






