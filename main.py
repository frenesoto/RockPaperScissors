import random
import time
import os
import colorama

from colorama import init
from colorama import Fore, Back
from random import randint
init()
os.system("clear")

print(Fore.GREEN + "Rock, Paper, Scissors!")
print(Fore.RED + "v.1.0 (by Pancho)\n")
print(Fore.BLUE + "Choose wisely")
print(Fore.RESET + "1. Stone")
print(Fore.RESET + "2. Scissors")
print(Fore.RESET + "3. Paper")

gameobject = input("Your answer (number): ")

if gameobject == "1":
    print ("\nYou have chosen Stone!")
    print ("The computer is choosing ... \n")
    time.sleep(2)
    cpugameobject = randint(1,3)
    if cpugameobject == 1:
        print(Fore.GREEN + "The computer chose Stone!, This is a draw!\n")
    elif cpugameobject == 2:
        print(Fore.GREEN + "The computer chose Scissors!, You've won!\n")
    elif cpugameobject == 3:
        print(Fore.GREEN + "The computer chose Paper!, You've lost!\n")

elif gameobject == "2":
    print ("\nYou have chosen Scissors!")
    print ("The computer is choosing ... \n")
    time.sleep(2)
    cpugameobject = randint(1,3)
    if cpugameobject == 1:
        print(Fore.GREEN + "The computer chose Stone!, You've lost!\n")
    elif cpugameobject == 2:
        print(Fore.GREEN + "The computer chose Scissors!, This is a draw!\n")
    elif cpugameobject == 3:
        print(Fore.GREEN + "The computer chose Paper!, You've won!\n")

elif gameobject == "3":
    print ("\nYou have chosen Paper!")
    print ("The computer is choosing ... \n")
    time.sleep(2)
    cpugameobject = randint(1,3)
    if cpugameobject == 1:
        print(Fore.GREEN + "The computer chose Stone!, You've won!\n")
    elif cpugameobject == 2:
        print(Fore.GREEN + "The computer chose Scissors!, You've lost!\n")
    elif cpugameobject == 3:
        print(Fore.GREEN + "The computer chose Paper!, This is a draw!\n")

time.sleep(2)