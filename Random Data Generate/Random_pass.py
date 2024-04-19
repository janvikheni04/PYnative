#Generate a random Password which meets the following conditions
#Password length must be 10 characters long.
#It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

import random
import string

def pass1():
    source = string.ascii_letters + string.digits + string.punctuation
    pwd = random.sample(source, 6)
    pwd += random.sample(string.ascii_letters, 2)
    pwd += random.choice(string.digits)
    pwd += random.choice(string.punctuation)

    pList = list(pwd)
    random.SystemRandom().shuffle(pList)
    pwd = ''.join(pList)
    return pwd

print("Random password is: ", pass1())