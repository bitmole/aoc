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
            numbers.append((n, s, e, i))
    return numbers

def list_adj_cells(n_rec, matrix):
    cells = []
    n, start, end, i = n_rec
    has_prev_row = i > 0
    has_next_row = i < len(matrix) - 1
    has_prev_col = start > 0
    has_next_col = len(matrix[i]) > end

    # above
    if has_prev_row:
        above = matrix[i-1]
        cells += above[start:end]
        print('above', cells)

    # below
    if has_next_row:
        below = matrix[i+1]
        cells += below[start:end]
        print('below', cells)

    # left
    if has_prev_col:
        left = [r[start-1] for r in matrix]
        s = i-1 if has_prev_row else i
        e = i+2
        cells += left[s:e]
        print('left', cells)

    # right
    if has_next_col:
        right = [r[end] for r in matrix]
        s = i-1 if has_prev_row else i
        e = i+2
        cells += right[s:e]
        print('right', cells)
        
    return cells

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
        self.assertEqual(numbers[0], ('467', 0, 3, 0))
        self.assertEqual(numbers[1], ('114', 5, 8, 0))
        self.assertEqual(numbers[2], ('35', 2, 4, 2))
        self.assertEqual(numbers[7], ('755', 6, 9, 7))

    def test_list_adj_cells(self):
        matrix = parse_matrix(self.test_input.splitlines())
        numbers = extract_numbers(matrix)
        n = numbers[6]
        cells = list_adj_cells(n, matrix)
        self.assertEqual(cells, ['.', '.', '.', '.', '.', '.','.', '.', '.', '+', '.', '.'])

if __name__ == "__main__":
    unittest.main()
