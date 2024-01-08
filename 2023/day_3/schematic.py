import unittest
import re

def parse_matrix(rows):
    matrix = []
    for r in rows:
        row = []
        for c in r:
            row.append(c)
        matrix.append(row)
    return matrix

def extract_numbers(matrix):
    numbers = []
    for i, r in enumerate(matrix):
        for m in re.finditer(r'(\d+)', ''.join(r)):
            n, s, e = m.group(0), m.start(), m.end()
            is_last_col = e == len(r)
            numbers.append((n, s, e, i, is_last_col))
    return numbers

def list_adjacents(numbers):
    pass

class KnownValues(unittest.TestCase):
    test_input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

    def test_parse_matrix(self):
        matrix = parse_matrix(self.test_input.splitlines())
        self.assertEqual(len(matrix), 10) 
        self.assertEqual(len(matrix[0]), 10) 
        self.assertEqual(matrix[0][2], '7') 

    def test_extract_numbers(self):
        matrix = parse_matrix(self.test_input.splitlines())
        numbers = extract_numbers(matrix)
        self.assertEqual(numbers[0], ('467', 0, 3, 0, False))
        self.assertEqual(numbers[1], ('114', 5, 8, 0, False))
        self.assertEqual(numbers[2], ('35', 2, 4, 2, False))
        self.assertEqual(numbers[7], ('755', 6, 9, 7, False))

if __name__ == "__main__":
    unittest.main()
