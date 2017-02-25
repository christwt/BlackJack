'''
    Black Jack Application
    main.py
    Author: William Christie
    copyright 2017 William Christie
    Last modified date: 2/2/17
'''

# import modules
from blackJackClass import BlackJackDeck

def rules():
    ''' display black jack rules and odds '''
    print("\nBlack Jack Rules!\n")
    print("Minimum bet is 5 chips")
    print("Black Jacks pay 3-2 odds")
    print("Regular wins give 2-1 odds")
    print("Dealer Black Jacks are instant wins for the house")
    print("Surrenders return 50% of the chips")
    print("To view rules: type h when asked for input")

def menu():
    ''' display menu options'''
    print("Menu:\nPlease use the keyboard to enter your choice\n\t",
          "r: to display Black Jack rules\n\t",
          "v: to view hand"
          "h: to hit\n\t",
          "s: to stand\n\t",
          "d: to double\n\t",
          "x: to surrender\n\t",
          "e: to end the game")

def main():
    ''' main function for black jack game '''
    print('\n\nWelcome to BlackJack!!!!\n\n')

    num_decks = int(input('Please enter the number of decks to use (1, 2, 6, 8)\n: '))

    unchecked = True
    while unchecked:
        if (num_decks == 1) or (num_decks == 2) or (num_decks == 6) or (num_decks == 8):
            unchecked = False
        else:
            num_decks = int(input("Error: Please enter the number of decks to ",
                                  "use (1, 2, 6, 8)\n: "))

    if num_decks == 1:
        print("You have selected to play BlackJack against the computer with",
              " " + str(num_decks) + " deck!\n\nDealing...")
    else:
        print("You have selected to play BlackJack against the computer with",
              " " + str(num_decks) + " decks!\n\nDealing...")

    print("You have been allocated 500 chips to start! Good luck!\n")

    game = BlackJackDeck(num_decks)
    game_not_done = True
    while game_not_done:

        game.deal()
        hand_not_done = True

        while hand_not_done:
            menu()
            choice = str(input("Select Your Choice"))
            choice.lower()
            if choice == "r":
                rules()
            elif choice == "v":
                game.viewhand()
            elif choice == "h":
                game.hit()
            elif choice == "s":
                game.endhand()
                hand_not_done = False


if __name__ == "__main__":
    main()

    