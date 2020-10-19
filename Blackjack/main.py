
import classes
import game_func
import globals_var

chips_check=0

while globals_var.game:
    # Print an opening statement
    print("\nHello and Welcome to Black Jack! Get as close to 21 before the dealer does! \nThe Dealer hits till they reach 17. Aces count for 11 or 1")

    
    # Create & shuffle the deck, deal two cards to each player
    deck=classes.Deck()
    deck.shuffle()
    
    player=classes.Hand()
    dealer=classes.Hand()
    
    for num in range(0,2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
        
    # Set up the Player's chips
    player_chips=classes.Chips() # Deafult Chips is set to 150
    
    if chips_check <=0:
        player_chips.rn_total = player_chips.total
    else:
        player_chips.rn_total = chips_check
    # Prompt the Player for their bet
    print(f'\nYou have a starting value of {player_chips.rn_total} chips ')
    game_func.take_bet(player_chips)

    
    # Show cards (but keep one dealer card hidden)
    game_func.show_some(player,dealer)
    
    while globals_var.playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        game_func.hit_or_stand(deck,player)
        
        # Show cards (but keep one dealer card hidden)
        game_func.show_some(player,dealer)
        input("\nPress Enter to Continue...")
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            game_func.player_busts(player_chips)
            chips_check = player_chips.rn_total
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value < 21:
        while dealer.value <= 17:
            dealer.add_card(deck.deal())
    
        # Show all cards
        game_func.show_all(player,dealer)


        # Run different winning scenarios
        if player.value > dealer.value:
            game_func.player_wins(player_chips)
            chips_check = player_chips.rn_total
        elif dealer.value > 21:
            game_func.dealer_busts(player_chips)
            chips_check = player_chips.rn_total
        elif dealer.value > player.value:
            game_func.dealer_wins(player_chips)
            chips_check = player_chips.rn_total
        else:
            game_func.push()
            chips_check = player_chips.rn_total  
    elif player.value == 21:
        game_func.player_wins(player_chips)
        chips_check = player_chips.rn_total

    input("\nPress Enter to Continue...")    
    play_check=True
    # Inform Player of their chips total 
    print(f'\nPlayer your chip total is: {player_chips.rn_total}')
    if player_chips.rn_total <=0:
        globals_var.playing=False
        play_check=False
        globals_var.game=False
        print("\nYou're out of chips!! Goodbye!!!")

    # Ask to play again
    while play_check:
        play_again=input("Would you like to play again? Please choose either 'y' or 'n'")
        
        if play_again.lower()=='y':
            globals_var.playing=True
            play_check=False
            
        elif play_again.lower()=='n':
            globals_var.playing=False
            play_check=False
            globals_var.game=False
            chips_check = 0
            #globals_var.whole_game=False
            print ("\nGoodbye!")
        else:
            print('Sorry that was a wrong entry! Please try again')
            play_check=True