# Kinda aids but ¯\_(ツ)_/¯

import base64
from time import sleep
from os import name, system

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

banner = """
  ____   __   _  _    
 | __ ) / /_ | || |  
 |  _ \| '_ \| || |_ 
 | |_) | (_) |__   _|
 |____/ \___/   |_|  

Options:

1 = Encode
2 = Decode
"""

result = """
  ____                 _ _   
 |  _ \ ___  ___ _   _| | |_ 
 | |_) / _ \/ __| | | | | __|
 |  _ <  __/\__ \ |_| | | |_ 
 |_| \_\___||___/\__,_|_|\__|
                             """

slashbars = """
////////////////////////////////////////////////////////////////
"""

def options():
    print(banner)
    lulz1 = input("Option: ")

    if lulz1 == "1":
        inputencode = input("String to Encode: ")
        #
        a = inputencode.encode('ascii')
        b = base64.b64encode(a)
        c = b.decode('ascii')
        #
        clear()
        print(result)
        print(slashbars)
        print(c)
        print(slashbars)
        sleep(7)
        clear()
        #
        options()
    elif lulz1 == "2":
        inputdecode = input("String to Decode: ")
        #
        a = inputdecode.encode('ascii')
        b = base64.b64decode(a)
        c = b.decode('ascii')
        #
        clear()
        print(result)
        print(slashbars)
        print(c)
        print(slashbars)
        sleep(7)
        clear()
        #
        options()
    else:
        print("Invalid Option")
        sleep(1.5)
        clear()
        options()

clear()
options()
