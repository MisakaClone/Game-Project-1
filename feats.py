# defining feats, which can have an impact on events

class Feat:
    def __init__(self, name, description, prerequisites, upgrade):
        self.name = name
        self.description = description
        self.prerequisites = prerequisites
        self.upgrade = upgrade

Intimidate = Feat('Intimidate',
                  'At the start of combat, if user\'s PHYS is higher than enemy\'s PHYS, enemy gains -1 STR.',
                  {'phys' : 26},
                  {'str' : 20}
                  )

Sturdy = Feat('Sturdy',
              'At the end of combat, user regains 15% missing health and loses 10% exhaustion.',
              {'cons' : 26},
              {'res' : 20}
              )

Cunning = Feat('Cunning',
               'When user is attacked, if user\'s REFL is higher than attacker\'s PHYS, attacker\'s attack counter is increased by 10. If this causes attacker to be hit, user\'s next attack critically strikes for +5 damage.',
               {'refl' : 26},
               {'spd' : 20}
               )

Resilience = Feat('Resilience',
                 'While below 75% health, user\'s PHYS is increased by 1 and attacks deal 1 more damage. While below 25% health, these bonuses are increased to 2 each.',
                 {'will' : 26},
                 {'foc' : 20}
                 )



