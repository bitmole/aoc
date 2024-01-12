import scratchcards as sc
import unittest

class KnownValues(unittest.TestCase):
    test_cards = '''
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    '''
    test_cards = [line.strip() for line in test_cards.splitlines() if line.strip()]

    def test_card_worth(self):
        expected = [8,2,2,1,0,0]
        for c in self.test_cards:
            self.assertEqual(sc.card_worth(c), expected.pop(0))

    def test_sum_card_pile(self):
        self.assertEqual(sc.sum_cards(self.test_cards), 13)

    def test_is_winning(self):
        expected = [(True, 4), (True, 2), (True, 2), (True, 1), (False, 0), (False, 0)]
        for card in self.test_cards:
            self.assertEqual(sc.is_winning(card), expected.pop(0))

    def test_process_all_losing_cards(self):
        cards = [ (False, 0), (False, 0), (False, 0), (False, 0), (False, 0) ]
        # should end up with the number of original cards as they win no copies
        self.assertEqual(sc.process(cards), len(cards))
        

if __name__ == "__main__":
    unittest.main()
