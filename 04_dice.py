import random

num_dice = input('How many die do you want to roll (limit 5)? ')
num_sides = input('How many sides per die? ')

for d in range(int(num_dice)):
    print(random.randrange(1, int(num_sides)))
