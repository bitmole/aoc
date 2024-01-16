# https://adventofcode.com/2023/day/4

import re

def card_worth(card):
    ncopies = n_winning_copies(card)
    if ncopies: 
        return pow(2, ncopies - 1)
    else: 
        return 0

def sum_cards(cards): return sum(card_worth(c) for c in cards)

def n_winning_copies(card):
    winning, hand = card.split('|')
    _, *winning = re.findall('\d+', winning) # throw away card number
    hand = re.findall('\d+', hand)
    winning_in_hand = set(winning) & set(hand) # intersection 
    return len(winning_in_hand)

def get_winning_copies(card, orig):
    s = orig.index(card) + 1
    e = s + n_winning_copies(card)
    return orig[s:e]

def map_won_copies(orig):
    return {c:get_winning_copies(c, orig) for c in orig}

def process_iter(cards):
    copies = map_won_copies(cards)

    for c in cards:
        cards += copies[c]

    return len(cards)

def process_recur(cards):
    copies = map_won_copies(cards)

    def sum_cards(cards):
        if not cards:
            return 0
        first, rest = cards[0], cards[1:]
        return 1 + sum_cards(rest) + sum_cards(copies[first])

    return sum_cards(cards)

def answers():
    cards = [line.strip() for line in open('input.txt').readlines()]
    print('total worth: ', sum_cards(cards))
    print('total cards (recur): ', process_recur(cards))
    print('total cards (iter): ', process_iter(cards))

if __name__ == "__main__":
    answers()
