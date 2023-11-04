import random

roll = random.randint(1,20)

print("You rolled a(n) " + str(roll))

if roll == 1:
    print("You failed")
elif roll > 1:
    print("Attack for " + str(roll))
