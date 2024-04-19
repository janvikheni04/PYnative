#Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
import random

lottery = []
for i in range(100):
    lottery.append(random.randrange(1000000000, 9999999999))
print(lottery)    

win = random.sample(lottery, 2)
print("lucky 2 winners are:", win)