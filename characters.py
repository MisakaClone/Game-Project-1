# defining classes for characters and enemies

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

# characters


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

charvars = [Colin, Tyler, Kay, Melody]

def charlist():
    listreturn = []
    for char in charvars:
        strengths = []
        for stat in char.stats:
            if char.stats.get(stat) == 10:
                weakness = stat

            elif char.stats.get(stat) == 13:
                strengths.append(stat)

            elif char.stats.get(stat) == 15:
                strengths.insert(0, stat)
                
        listreturn.append({'name' : char,
                           'strengths' : strengths,
                           'weakness' : weakness
                          })
    return listreturn

