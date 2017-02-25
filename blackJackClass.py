'''
    Black Jack Application
    main.py
    Author: William Christie
    copyright 2017 William Christie
    Last modified date: 2/2/17
'''
# import necessary modules
from random import randint

# Set Constants
CONST_DECK_TOTAL = 52
CONST_SUIT_COUNT = 4

# Black Jack Game Class
class BlackJackDeck:
    ''' black jack deck class for game'''

    def draw(self):
        ''' Draw a card from the deck '''
        card = randint(2, 11)
        return card

    def __init__(self, number):
        ''' intial deck setup, set counts and initialize hand '''
        # card counts
        self.deckcount = number * CONST_DECK_TOTAL
        self.acecount = number * CONST_SUIT_COUNT
        self.twocount = number * CONST_SUIT_COUNT
        self.threecount = number * CONST_SUIT_COUNT
        self.fourcount = number * CONST_SUIT_COUNT
        self.fivecount = number * CONST_SUIT_COUNT
        self.sixcount = number * CONST_SUIT_COUNT
        self.sevencount = number * CONST_SUIT_COUNT
        self.eightcount = number * CONST_SUIT_COUNT
        self.ninecount = number * CONST_SUIT_COUNT
        self.tencount = number * CONST_SUIT_COUNT
        self.jackcount = number * CONST_SUIT_COUNT
        self.queencount = number * CONST_SUIT_COUNT
        self.kingcount = number * CONST_SUIT_COUNT
        # establish user hand
        self.hand_user = []
        # establish dealer hand
        self.hand_dealer = []
        # user chip count to start game
        self.chipcount = 500

    def deal(self):
        ''' draw 2 from the deck from deck '''
        # user
        card1_user = self.draw()
        card1_user = self.adjustcounts(card1_user)
        card2_user = self.draw()
        card2_user = self.adjustcounts(card2_user)
        self.hand_user.extend([card1_user, card2_user])

        # dealer
        card1_dealer = self.draw()
        card1_dealer = self.adjustcounts(card1_dealer)
        card2_dealer = self.draw()
        card2_dealer = self.adjustcounts(card2_dealer)
        self.hand_dealer.extend([card1_dealer, card2_dealer])

    def adjustcounts(self, card):
        ''' adjust counts in deck and re-do random draw if necessary '''
        if card == 11 and self.acecount > 0:
            self.acecount -= 1
            return card
        elif card == 10:
            if self.kingcount > 0:
                self.kingcount -= 1
                return card
            elif self.queencount > 0:
                self.queencount -= 1
                return card
            elif self.jackcount > 0:
                self.jackcount -= 1
                return card
            elif self.tencount > 0:
                self.jackcount -= 1
                return card
        elif card == 9 and self.ninecount > 0:
            self.ninecount -= 1
            return card
        elif card == 8 and self.eightcount > 0:
            self.eightcount -= 1
            return card
        elif card == 7 and self.sevencount > 0:
            self.sevencount -= 1
            return card
        elif card == 6 and self.sixcount > 0:
            self.sixcount -= 1
            return card
        elif card == 5 and self.fivecount > 0:
            self.fivecount -= 1
            return card
        elif card == 4 and self.fourcount > 0:
            self.fourcount -= 1
            return card
        elif card == 3 and self.threecount > 0:
            self.threecount -= 1
            return card
        elif card == 2 and self.twocount > 0:
            self.twocount -= 1
            return card
        else:
            # too many boolean in if statement: refactor into array and search array?
            if (self.acecount == 0 and self.twocount == 0 and self.threecount == 0
                    and self.fourcount == 0 and self.fivecount == 0 and self.sixcount == 0
                    and self.sevencount == 0 and self.eightcount == 0 and self.ninecount == 0
                    and self.tencount == 0):
                    # shuffle
                print("Shuffling...")
                    # TODO: shuffle function required to reset the deck
                card = self.draw()
                self.adjustcounts(card)
            else:
                # continue
                card = self.draw()
                self.adjustcounts(card)

    def hit(self, identity):
        ''' draw another card from the deck, add to hand '''
        card = self.draw()
        card = self.adjustcounts(card)
        if identity == 1:
            self.hand_user.append(card)
        elif identity == 2:
            self.hand_dealer.append(card)

    def viewhand(self, identity):
        ''' view current hand and give total '''
        total = 0
        iterator = 0

        if identity == 1:
            hand = self.hand_user
        elif identity == 2:
            hand = self.hand_dealer
        
        print("In your current hand:\n")

        for card in hand:
            iterator += 1
            print("Card " + str(iterator) + " gives you: " + str(card) + " points")
            total += card
        
        print("Your current total is: " + str(total) + " points")

        return total
    
    def endhand(self, action):
        ''' ends hand called by stay, surrender, or overage, updates chip totals '''
        card_total_user = self.viewhand(1)
        card_total_dealer = self.viewhand(2)

        if action == "s" or action == "S":
            if card_total_user > card_total_dealer:
                print("Winner!")
                self.chipcount += 5
            else:
                print("Loser!")
                self.chipcount -= 5 
        elif action == "b":
            print("BlackJack! Congratulations!")
            self.chipcount += 7.5
            print("Current chip count: " + str(self.chipcount))
        elif action == "o":
            print("You're over 21! BUST!")
            self.chipcount -= 5
        elif action == "x":
            print("Surrender: returns 50% of chips")
            self.chipcount += 2.5

    def endgame(self):
        ''' end game, call destructor '''
        print("Ending Game:")
        