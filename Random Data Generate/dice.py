#Roll dice in such a way that every time you get the same number
import random

dice = [1,2,3,4,5,6]
print("Random number every time on same number")

for i in range(5):
    random.seed(25)
    print(random.choice(dice))