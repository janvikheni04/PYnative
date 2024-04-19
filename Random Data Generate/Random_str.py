#Generate random String of length 5

import random
import string

def randStr(Strlen):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(Strlen))

print("Random string is:", randStr(5))