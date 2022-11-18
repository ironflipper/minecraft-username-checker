import requests
import string
import random
import time
import os

os.system('color')

class bcolors:
    HEADER = '\033[95m'
    OKRED = '\033[31m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print()
print("How many letters should the generated usernames have? (At least 3!)")
letterz = input()
print()

while True:

    letters = string.ascii_lowercase + string.digits
    name = ( ''.join(random.choice(letters) for i in range(int(letterz))) )
    
    response = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name + "?at=%3Ctimestamp%3E")

    if str(response) == '<Response [204]>':
        print(bcolors.OKGREEN)
        print(response)
        print(name)
        print(bcolors.ENDC)
        
        f = open("usernames.txt", "a")
        f.write(name + "\n")
        f.close()

        time.sleep(10)
    elif str(response) == '<Response [429]>':
        print(bcolors.OKRED)
        print(response)
        print(name)
        print(bcolors.ENDC)
        time.sleep(60)
    else:
        print(response)
        print(name)
        time.sleep(0.2)
