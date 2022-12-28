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
    pass

# defining character classes

class Character:
    def __init__(self, name, pronouns, stats):
        self.name = name
        self.pronouns = pronouns
        self.stats = stats

        self.str = stats['str']
        self.spd = stats['spd']
        self.foc = stats['foc']
        self.res = stats['res']

        self.phys = stats['str'] + stats['spd']
        self.refl = stats['spd'] + stats['foc']
        self.will = stats['foc'] + stats['res']
        self.cons = stats['res'] + stats['str']


Colin = Character('Colin',
                 {'pers' : 'he',
                  'obj' : 'him',
                  'adj' : 'his',
                  'poss' : 'his',
                  'refl' : 'himself'},
                 {'str': 13, 'spd' : 10, 'foc' : 12, 'res' : 15}
                 )
Tyler = Character('Tyler',
                 {'pers' : 'they',
                  'obj' : 'them',
                  'adj' : 'their',
                  'poss' : 'theirs',
                  'refl' : 'themself'},
                 {'str': 10, 'spd' : 12, 'foc' : 15, 'res' : 13}
                 )
Kay = Character('Kay',
               {'pers' : 'she',
                'obj' : 'her',
                'adj' : 'her',
                'poss' : 'hers',
                'refl' : 'herself'},
               {'str': 12, 'spd' : 15, 'foc' : 13, 'res' : 10}
               )
Melody = Character('Melody',
                  {'pers' : 'she',
                   'obj' : 'her',
                   'adj' : 'her',
                   'poss' : 'hers',
                   'refl' : 'herself'},
                  {'str': 15, 'spd' : 13, 'foc' : 10, 'res' : 12}
                  )

#character select

select_Success = False

while not select_Success:
    charc = input('''\nSelect your character:\n
1) Colin (He/Him)      Strengths:RES, STR  Weakness:SPD\n
2) Tyler (They/Them)   Strengths:FOC, RES  Weakness:STR\n
3) Kay (She/Her)       Strengths:SPD, FOC  Weakness:RES\n
4) Melody (She/Her)    Strengths:STR, SPD  Weakness:FOC\n''')


    try:
        if int(charc) not in range(1, 5):
            raise indexError
        else:
            select2_Success = False

            while not select2_Success:
                
                if int(charc) == 1:
                    verif = input('''Colin:\n
STR: {} {}
SPD: {} {}
FOC: {} {}
RES: {} {}

Select Colin?
1) Yes     2) No\n'''.format(Colin.str, ''.ljust(Colin.str,'■'),
                     Colin.spd, ''.ljust(Colin.spd,'■'),
                     Colin.foc, ''.ljust(Colin.foc,'■'),
                     Colin.res, ''.ljust(Colin.res,'■'),))

                    try:
                        if int(verif) not in [1,2]:
                            raise indexError
                        
                        else:
                            if int(verif) == 1:
                                charc = Colin
                                select_Success = True
                                select2_Success = True
                            elif int(verif) == 2:
                                select2_Success = True

                    except:
                        print('Please choose 1 or 2')
                    
                elif int(charc) == 2:
                    verif = input('''Tyler:\n
STR: {} {}
SPD: {} {}
FOC: {} {}
RES: {} {}

Select Tyler?
1) Yes     2) No\n'''.format(Tyler.str, ''.ljust(Tyler.str,'■'),
                     Tyler.spd, ''.ljust(Tyler.spd,'■'),
                     Tyler.foc, ''.ljust(Tyler.foc,'■'),
                     Tyler.res, ''.ljust(Tyler.res,'■'),))

                    try:
                        if int(verif) not in [1,2]:
                            raise indexError
                        
                        else:
                            if int(verif) == 1:
                                charc = Tyler
                                select_Success = True
                                select2_Success = True
                            elif int(verif) == 2:
                                select2_Success = True

                    except:
                        print('Please choose 1 or 2')
                
                elif int(charc) == 3:
                    verif = input('''Kay:\n
STR: {} {}
SPD: {} {}
FOC: {} {}
RES: {} {}

Select Kay?
1) Yes     2) No\n'''.format(Kay.str, ''.ljust(Kay.str,'■'),
                     Kay.spd, ''.ljust(Kay.spd,'■'),
                     Kay.foc, ''.ljust(Kay.foc,'■'),
                     Kay.res, ''.ljust(Kay.res,'■'),))

                    try:
                        if int(verif) not in [1,2]:
                            raise indexError
                        
                        else:
                            if int(verif) == 1:
                                charc = Kay
                                select_Success = True
                                select2_Success = True
                            elif int(verif) == 2:
                                select2_Success = True

                    except:
                        print('Please choose 1 or 2')
                
                elif int(charc) == 4:
                    verif = input('''Melody:\n
STR: {} {}
SPD: {} {}
FOC: {} {}
RES: {} {}

Select Melody?
1) Yes     2) No\n'''.format(Melody.str, ''.ljust(Melody.str,'■'),
                     Melody.spd, ''.ljust(Melody.spd,'■'),
                     Melody.foc, ''.ljust(Melody.foc,'■'),
                     Melody.res, ''.ljust(Melody.res,'■'),))

                    try:
                        if int(verif) not in [1,2]:
                            raise indexError
                        
                        else:
                            if int(verif) == 1:
                                charc = Melody
                                select_Success = True
                                select2_Success = True
                            elif int(verif) == 2:
                                select2_Success = True

                    except:
                        print('Please choose 1 or 2')
    except:
        print('Please choose 1, 2, 3, or 4')

print('\nYou are playing as {}'.format(charc.name))



