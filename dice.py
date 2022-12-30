# dice
import random

class Dice:
    def __init__(self, pool):
        self.sides = len(pool)
        self.pool = pool

    def roll(self):
        return random.choice(self.pool)

    

d4 = Dice(range(1,5))
d6 = Dice(range(1,7))
d8 = Dice(range(1,9))
d10 = Dice(range(1,11))
d20 = Dice(range(1,21))
    


