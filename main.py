'''
    Black Jack Application
    Author: William Christie
    copyright 2017 William Christie
    Last modified date: 1/30/17
'''
# Import modules
from random import randint

# Set Constants
CONST_DECK_NUM = 52
CONST_FACE_CARD_COUNT = 16
CONST_ACE_COUNT = 4
CONST_NUM_CARD_COUNT = 52 - 16 - 4

class BlackJackDeck:
    ''' black jack deck class for game'''

    def draw(self):
        ''' Draw a card from the deck '''
        card = randint(2, 11)
        return card

    def __init__(self, number):
        ''' intial deck setup '''
        self.deckcount = number * CONST_DECK_NUM
        self.facecount = number * CONST_FACE_CARD_COUNT
        self.acecount = number * CONST_ACE_COUNT
        self.numcount = number * CONST_NUM_CARD_COUNT
        self.hand = []
        self.chipcount = 500

    def deal(self):
        ''' draw 2 from the deck from deck '''
        card1 = self.draw()
        card2 = self.draw()

        self.hand.extend([card1, card2])

        # ace handling here?


    def hit(self):
        ''' draw another card from the deck, add to hand '''
        card = self.draw()
        self.hand.append(card)

    def viewhand(self):
        ''' view current hand and give total '''
        total = 0
        iterator = 0

        print('/nIn your current hand:/n')

        for card in self.hand:
            print('Card ' + str(iterator + 1) + ' gives you ' + str(self.hand[card-1]) + ' points')
            total += self.hand[card-1]

        if total > 21:
            print('Ouch! You\'re over 21 points!')
        else:
            print('Your current total points is: ' + str(total))
        
        return total
    
    def endhand(self):
        ''' ends hand called by stay, surrender, or overage, updates chip totals '''
        card_total = self.viewhand()

            # if dealer > user, lose
            # if dealer < user, win
            # if dealer = user, win
        


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
        print("You have selected to play BlackJack against the computer with ",
              + str(num_decks) + " deck!\n\nDealing...")
    else:
        print("You have selected to play BlackJack against the computer with ",
              + str(num_decks) + " decks!\n\nDealing...")

    print("You have been allocated 500 chips to start the game! Good luck!")

    game = BlackJackDeck(num_decks)
    game.deal()

    game.viewhand()

if __name__ == "__main__":
    main()

    