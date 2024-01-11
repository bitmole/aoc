import re

def card_worth(card):
    winning, hand = card.split('|')
    winning = re.findall('\d+', winning)[1:] # throw away card number
    hand = re.findall('\d+', hand)

    # holding any winning numbers?
    winning_in_hand = set(winning).intersection(set(hand))
    if winning_in_hand: 
        exp = len(winning_in_hand) - 1
        return pow(2, exp)
    else: 
        return 0
