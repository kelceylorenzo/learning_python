from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))


six_sided = Die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()

print('\n')

ten_sided = Die(10)
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()

print('\n')

twenty_sided = Die(20)
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()