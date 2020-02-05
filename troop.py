import os
import sys
from time import sleep as timeout
from core.starkmcore import *
from multiprocessing import Process
from termcolor import colored

checkfile()
def menu():
    os.system("clear")
    print(colored("""
         ──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
			    5.2(BETA)
>> CREATED BY: TROOPEKYT 
>> Youtube:   TROOPEK
>> Instagram: @Troopek
>>>ONLY FOR TERMUX<<<

===============================================
1. Basic Command
2. Account Penatration
3. Website Penetration
4. Hash Cracker
5. Termux
6. Error Fixer
7. Credits
8. Follow Me!
9. Open Old Stark2.0
================================================
10. EXIT
""", 'green'))

loop = True

while loop:
    menu()
    Troop = raw_input("troop > ")

    if troop == "1":
          os.system("clear")
          BasicC()
    elif troop == "2":
          os.system("clear")
          AccountH()
    elif troop == "3":
          os.system("clear")
          WebH()
    elif troop == "4":
          os.system("clear")
          HASH()
    elif troop == "5":
          os.system("clear")
          Termux()
    elif troop == "6":
          EFixer()
    elif troop == "7":
          Credits()
    elif troop == "8":
         os.system("clear")
         follow()
    elif troop == "9":
	 os.system("cd modules/TROOP/ && python2 troop.py")
    elif troop == "10":
        sys.exit()
    elif troop == "0":
          reset()
    else:
                  print  (colored("ERROR: WRONG COMMAND BROOO.?", 'red'))
                  timeout(2)
                  reset()
