import re

def card_worth(card):
    print(card)
    winning, hand = card.split('|')
    winning = re.findall('\d+', winning)[1:] # throw away card number
    hand = re.findall('\d+', hand)
    worth = 0
    for n in hand:
        if n in winning:
            worth = 1 if worth==0 else 2*worth

    return worth
