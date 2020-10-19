import globals_var



def take_bet(chips):
    
    while True:
        try:
            chips.bet= int(input('\nHow many chips would you like to bet? '))
        except ValueError:
            print('Sorry that is an invalid entry. Integer values only please!')
        else:
            if chips.bet > chips.rn_total:
                print(f'Sorry that amount is more than you have. You have {chips.rn_total} chips. Try a lower amount!')
            elif chips.bet <=0:
                print("Sorry the value has to be a positive integer! Please try again")
            elif chips.bet <= chips.rn_total:
                print(f'Sounds good! You have bet {chips.bet} chips')
                break
           


def hit(deck,hand):
    
    hand.add_card(deck.deal()) #adds a card from deck to the hand
    hand.adjust_for_ace() #changes the value of hand if aces exist and over 21


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    #Using the Try with While loop is redundant here. We are looking for str values. Input func converts to str
    #by default so any value will be converted hence no error for Except to check for.
    #Use a While loop with simple If statements next time
    
    while True:
        try:
            play_choice= input("\nWould you like to Hit or Stand? Please input 'h' or 's': ")
        except ValueError:
            print('Wrong Input try again!')
        else:   
            if play_choice !='h' and play_choice !='s':
                print ('Wrong Input try again!')
                
            else:
                break
        
    if play_choice.lower() == 'h':
        hit(deck,hand)
    elif play_choice.lower() == 's':
        print('Player Stands. Dealer is playing.')
        globals_var.playing = False
        
    #return playing        


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <Hidden Card>")
    print(" ",dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep= '\n ') #The * will insert the sep between each item in list
    
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep= '\n ')
    print("\nDealer's Hand" , dealer.value, sep= '=')
    print("\nPlayer's Hand:", *player.cards, sep= '\n ')
    print("\nPlayer's Hand" , player.value, sep= '=')


def player_busts(chips):
    print('\nPlayer Busts!')
    chips.lose_bet()

def player_wins(chips):
    print('\nPlayer Wins!')
    chips.win_bet()

def dealer_busts(chips):
    print('\nDealer Busts!, Player Wins!')
    chips.win_bet()
    
def dealer_wins(chips):
    print('\nDealer Wins!')
    chips.lose_bet()
    
def push():
    print("\nPlayer and Dealer Tie. It's a Push")        