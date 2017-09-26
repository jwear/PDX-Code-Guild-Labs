import random
import os
os.system('clear')

num_dice = input("Let's roll some dice! How many dice do you want to roll?\n")
num_sides = input("How many sides per die?\n")

print("Let's roll... ")
for d in range(int(num_dice)):
    print(random.randrange(1, int(num_sides)))
