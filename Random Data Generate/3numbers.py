#Generate 3 random integers between 100 and 999 which is divisible by 5
import random
print("Generate 3 randomnumbers btw 100 and 999 divisible by 5")

for i in range(3):
    print(random.randrange(100,999,5), end =',')