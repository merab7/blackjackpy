import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def add_card(hand):
    card_value = random.choice(cards)
    if card_value == 11 and sum(hand) + 11 <= 21:
        hand.append(11)
    elif card_value == 11 and sum(hand) + 11 > 21:
        hand.append(1)    
    else:
        hand.append(card_value)

def determine_winner(player_cards, dealer_cards):
    player_score = sum(player_cards)
    dealer_score = sum(dealer_cards)

    if player_score <= 21 and dealer_score > 21:
        return "You won!"
    elif 21 >= player_score > dealer_score:
        return "You won!"
    elif player_score == dealer_score:
        return "It's a draw!"
    else:
        return "You lost!"