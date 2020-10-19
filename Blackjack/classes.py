import random

#Tuples to store Suits and Ranks names
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

#Need a dictionary to link the Rank names with respective Values
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}




class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return (f'{self.rank} of {self.suit}')


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))#Build Card objects to store in list
    
    def __str__(self):
        deck_str='' #Empty string
        for card in self.deck:
            deck_str+= '\n' + card.__str__()
        return f'The Deck Contains {deck_str}'
        

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        playcard=self.deck.pop()
        return playcard


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+= values[card.rank]
        
        if card.rank=="Ace":
            self.aces+=1 #Counter for number of Aces in a hand
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value-=10
            self.aces-=1




class Chips:
    
    def __init__(self):
        self.total = 150  # This can be set to a default value or supplied by a user input
        self.rn_total= 0
        self.bet = 0
        
    def win_bet(self):
        self.rn_total+=self.bet
    
    def lose_bet(self):
        self.rn_total-=self.bet
        
    def __str__(self): #String value to see number of chips available
        return f'You have {self.total} chips'



        