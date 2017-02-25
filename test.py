'''
    Black Jack Application
    test.py
    Author: William Christie
    copyright 2017 William Christie
    Last modified date: 2/2/17
'''

# import necessary modules
from blackJackClass import BlackJackDeck
import unittest

complete = True

while complete:
    choice = int(input("select 1 2 3 4"))
    if choice == 1:
        print(choice)
    elif choice == 2:
        print(choice)
    elif choice == 3:
        print(choice)
    elif choice == 4:
        print(choice)
        complete = False
    else:
        print("incorrect selection, start again")

print("loop complete")





