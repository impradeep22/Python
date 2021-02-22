import random

print("Welcome to the Dice Stimulator.\n Rules: \n1. Enter y to roll the dice again. \n2. Enter any other aplphabet or number to exit the stimulator.")

x='y'

while x == 'y':
    diceNumber = random.randint(1,6)
    if diceNumber == 1:
        print('----------')
        print('|         |')
        print('|    O    |')
        print('|         |')
        print('----------')
    if diceNumber == 2:
        print('----------')
        print('|         |')
        print('| O     O |')
        print('|         |')
        print('----------')
    if diceNumber == 3:
        print('----------')
        print('| O       |')
        print('|    O    |')
        print('|       O |')
        print('----------')
    if diceNumber == 4:
        print('----------')
        print('| O     O |')
        print('|         |')
        print('| O     O |')
        print('----------')
    if diceNumber == 5:
        print('----------')
        print('| O     O |')
        print('|    O    |')
        print('| O     O |')
        print('----------')
    if diceNumber == 6:
        print('----------')
        print('| O     O |')
        print('| O     O |')
        print('| O     O |')
        print('----------')
    x = input("Enter y to roll the Dice again:")
