import dice

# weapons and items

class Item:
    def __init__(self, name, description, effects, value, damage = None):
        self.name = name
        self.description = description
        self.value = value
        self.effects = effects
        self.damage = None


class Weapon(Item):
    def __init__(self, name, damage, description, effects, value):
        Item.__init__(self, name, description, effects, value)
        self.damage = damage
        

Sword = Weapon('Old Sword',
               dice.d4,
               'An old sword that looks like it\'s about to fall apart',
               'Adds a d4 to your damage.',
               5
               )

Claws = Weapon('Claws',
               dice.d4,
               'The claws of a large bear',
               'Adds a d4 to your damage.',
               0
               )



weaponList = [eval(i) for i in dir() if type(eval(i)) == Weapon]
itemList = [eval(i) for i in dir() if type(eval(i)) in [Item] + [cls for cls in Item.__subclasses__()]]


def wSeek(weap):
    for i in weaponList:
        if i.name == weap:
            return i

def iSeek(item):
    for i in itemList:
        if i.name == item:
            return i
