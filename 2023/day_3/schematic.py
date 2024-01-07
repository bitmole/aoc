import unittest

def parse_matrix(rows):
    matrix = []
    for r in rows:
        row = []
        for c in r:
            row.append(c)
        matrix.append(row)
    return matrix

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

if __name__ == "__main__":
    unittest.main()
