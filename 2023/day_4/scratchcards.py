import re

def card_worth(card):
    winning, nmatches = is_winning(card)
    if winning: 
        return pow(2, nmatches - 1)
    else: 
        return 0

def sum_cards(cards):
    return sum(card_worth(c) for c in cards)

def is_winning(card):
    winning, hand = card.split('|')
    winning = re.findall('\d+', winning)[1:] # throw away card number
    hand = re.findall('\d+', hand)
    winning_in_hand = set(winning).intersection(set(hand))
    nmatches = len(winning_in_hand)
    return nmatches > 0, nmatches

def process(cards):
    if not cards:
        return 0
    wins, nmatches = cards[0]
    if not wins:
        return 1 + process(cards[1:])
    else:
        #TODO: process next nmatches cards
        return 0


def answers():
    cards = (line.strip() for line in open('input.txt').readlines())
    print('total worth: ', sum_cards(cards))

if __name__ == "__main__":
    answers()
