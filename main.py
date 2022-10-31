# Import logo
from black_jack_art import logo
# Import random
import random
# CLS commands do not work with IDE used to write this program. clear function used as substitute
def clear():
    print(100 * "\n")
# This game will assume there is an unlimited deck to use
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Define other lists and variables
dealer_hand = []
dealer_score = 0
player_hand = []
player_score = 0
player_chips = 500
bet = 0
play = True
dealer_done = False
# Place bet function set to grab input for betting amount
def place_bet():
    global bet
    while True:
        try:
            bet_try = int(input(f"Place your bet. You have ${player_chips} in chips to use. "))
        except:
            print("Please re-enter your bet using no letters or symbols. Only numbers.")
            continue
        if bet_try > player_chips:
            print("Your bet is higher than the amount of chips you have. Please re-enter a smaller bet.")
            continue        
        elif bet_try <= 0:
            print("You cannot bet on yourself to lose. Please enter a positive bet.")
            continue
        else:
            bet += bet_try
            break
# Continue game function set to be triggered after result of each round to continue while loop
def continue_game():
    global play
    while True:
        play_response = input("Do you want to play another round of Blackjack? Type 'y' or 'n': ").lower()
        if play_response == 'y':
            play = True
            break
        elif play_response == 'n':
            if player_chips > 500:
                print(f"You are one of the few who walk away up in chips with a total of ${player_chips}. Great job!")
            elif player_chips == 500:
                print("You walk away with no damage done to your chip stash. Not bad!")
            elif player_chips < 500:
                print(f"Darn! You walk away down to a total of ${player_chips}.")
            play = False
            break
        else:
            print("I'm sorry, please give a response of 'y' or 'n'.")
# Deal card dealer function set to deal one card to the dealer's hand when called upon
def deal_card_dealer():
    global dealer_hand
    global dealer_score
    dealer_card = random.choice(cards)   
    dealer_hand.append(dealer_card)
    dealer_score += dealer_card
# Deal card player function set to deal one card to the player's hand when called upon    
def deal_card_player():
    global player_hand
    global player_score
    player_card = random.choice(cards)  
    player_hand.append(player_card)
    player_score += player_card
# Start game function set to clear previous shell script, display Blackjack logo, deal cards to both player and dealer, and ask for betting input
def start_game():
    clear()
    print(logo)
    deal_card_player()
    deal_card_player()
    deal_card_dealer()
    deal_card_dealer()
    place_bet()
# Win game function set to trigger message outputs, change player chips amount, and clear variables for potential next round
def win_game():
    global player_hand
    global player_score
    global dealer_hand
    global dealer_score
    global player_chips
    global bet
    print(f"Your final hand: {player_hand}, final score: {player_score}.")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}.")
    print(f"You win ${bet} this round!")
    player_chips += bet
    bet = 0
    player_hand = []
    player_score = 0
    dealer_hand = []
    dealer_score = 0
# Lose game function set to trigger mesage outputs, change player chips amount, and clear variables for potential next round
def lose_game():
    global player_hand
    global player_score
    global dealer_hand
    global dealer_score
    global player_chips
    global bet
    print(f"Your final hand: {player_hand}, final score: {player_score}.")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}.")
    print("Dealer wins!")
    player_chips -= bet
    bet = 0
    player_hand = []
    player_score = 0
    dealer_hand = []
    dealer_score = 0
# Tie game function set to trigger message outputs and clear variables for potential next round
def tie_game():    
    global player_hand
    global player_score
    global dealer_hand
    global dealer_score
    global bet
    print(f"Your final hand: {player_hand}, final score: {player_score}.")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}.")
    print("Push")
    bet = 0
    player_hand = []
    player_score = 0
    dealer_hand = []
    dealer_score = 0
# No more chips function set to display final message when player runs out of chips; code ends
def no_more_chips():
    if player_chips == 0:
            print("You ran out of chips! Better luck next time.")
            exit()
# Blackjack round starts again if player says yes to another round
while play == True:
    start_game()
#     Early condition set if player is dealt a winning starting hand
    if player_score == 21:
        while True:
            if dealer_score == 21:
                break
            elif dealer_score >= 17:
                if dealer_score > 21:
#                     Final condition to save dealer's hand checking for an ace
                    if 11 in dealer_hand:
                        for i in range(len(dealer_hand)):
                            if dealer_hand[i] == 11:
                                dealer_hand[i] = 1
                                dealer_score -= 10
#                 Dealer stands if hand is scored 17 or higher
                break
#             Dealer draws another card if hand is scored 16 or below
            else:
                deal_card_dealer()
                continue
# If player and dealer both score 21, result is tie
        if player_score == dealer_score:
            tie_game()
            no_more_chips()
            continue_game()
            continue
# Player holds a blackjack and wins 
        else:
            win_game()
            no_more_chips()
            continue_game()
            continue
# While loop continuation past lucky blackjack starting hand condition
    print(f"Your cards: {player_hand}, current score: {player_score}.")
    print(f"Computer's first card: {dealer_hand[0]}.")
# Nested while loop for player to hit or stand
    while True:
#         Dealer done variable used to break out of two while loops
        if dealer_done == True:
            dealer_done = False
            break
        hit_or_stand = input("Type 'y' to get another card, type 'n' to stand: ").lower()
        if hit_or_stand != 'y' and hit_or_stand != 'n':
            print("I'm sorry, please give a response of 'y' or 'n'.")
            continue
        if hit_or_stand == 'y':
            deal_card_player()
            if player_score > 21:
                if 11 in player_hand:
                    for i in range(len(player_hand)):
                        if player_hand[i] == 11:
                            player_hand[i] = 1
                            player_score -= 10
                else:
                    break
            print(f"Your cards: {player_hand}, current score: {player_score}.")
            continue
        elif hit_or_stand == 'n':
            while True:
                if dealer_score >= 17: 
                    if dealer_score > 21:
                        if 11 in dealer_hand:
                            for i in range(len(dealer_hand)):
                                if dealer_hand[i] == 11:
                                    dealer_hand[i] = 1
                                    dealer_score -= 10
                    dealer_done = True
                    break
                else:
                    deal_card_dealer()
                    continue
# Player overdraws and scores over 21; loses
    if player_score > 21:
        lose_game()
        no_more_chips()
        continue_game()
        continue
# Player's score is greater than dealer's score (excludes scores over 21 for player)
    if player_score > dealer_score:
        win_game()
        no_more_chips()
        continue_game()
        continue
# Dealer overdraws and scores over 21; win for player
    if dealer_score > 21:
        win_game()
        no_more_chips()
        continue_game()
        continue
# Dealer outdraws player and ends up with the highest score; player loses
    if player_score < dealer_score:
        lose_game()
        no_more_chips()
        continue_game()
        continue
# If player and dealer both score the same, result is tie
    if player_score == dealer_score:
        tie_game()
        continue_game()
        continue
            
        
            
        

