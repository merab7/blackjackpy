import random
import sys
from utiles import add_card
from utiles import determine_winner
from utiles import cards
from logo import logo




def play():
    print(logo)
    do_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()

    if do_play not in ["y", "n"]:
        print("You only have two options: 'y' or 'n'")
        return play()

    if do_play == "n":
        sys.exit()
    else:
        player_cards = [random.choice(cards) for _ in range(2)]
        dealer_cards = [random.choice(cards) for _ in range(2)]
        
        while True:
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}\nComputer's first card: {dealer_cards[0]}")
            continue_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if continue_game not in ["y", "n"]:
                print("You only have two options: 'y' or 'n'")
                continue

            if continue_game == "n":
                winner = determine_winner(player_cards, dealer_cards)
                print(f"{winner}\nYour cards are: {player_cards}\nyour score:{sum(player_cards)}\nComputer cards are: {dealer_cards}\ncomputer score:{sum(dealer_cards)}")
                def again () :
                    play_again = input("If you want to play again press Y or N to exit:  ").lower()
                    if play_again not in ["y", "n"]:
                        print("You only have two options: 'y' or 'n'")
                        return again()
                    elif play_again == "y" :
                        return play()
                    else :
                       sys.exit()
                again()    
            else:
                add_card(player_cards)
                add_card(dealer_cards)

if __name__ == "__main__":
    play()
