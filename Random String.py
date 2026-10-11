import random
import string

def randomString(stringLength):
    letter = string.ascii_letters
    return ''.join(random.choice(letter) for i in range(stringLength))

print ("Random String is:  ", randomString(7) )
