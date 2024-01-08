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

    # below
    if has_next_row:
        below = matrix[i+1]
        cells += below[start:end]

    # left
    if has_prev_col:
        left = [r[start-1] for r in matrix]
        s = i-1 if has_prev_row else i
        e = i+2
        cells += left[s:e]

    # right
    if has_next_col:
        right = [r[end] for r in matrix]
        s = i-1 if has_prev_row else i
        e = i+2
        cells += right[s:e]
        
    return cells

def sum_part_numbers(matrix):
    numbers = extract_numbers(matrix)
    part_numbers = [int(n[0]) for n in numbers if is_part_number(n, matrix)]
    return sum(part_numbers)

def is_part_number(n, matrix):
    cells = list_adj_cells(n, matrix)
    return any(is_symbol(c) for c in cells)

def is_symbol(c):
    return (not c.isalnum() and c != '.')

def main():
    input_lines = [l.strip() for l in open('input.txt').readlines()]
    matrix = parse_matrix(input_lines)
    print('total:', sum_part_numbers(matrix))

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
    matrix = parse_matrix(test_input.splitlines())

    def test_extract_numbers(self):
        numbers = extract_numbers(self.matrix)
        self.assertEqual(numbers[0], ('467', 0, 3, 0))
        self.assertEqual(numbers[1], ('114', 5, 8, 0))
        self.assertEqual(numbers[2], ('35', 2, 4, 2))
        self.assertEqual(numbers[7], ('755', 6, 9, 7))

    def test_list_adj_cells(self):
        numbers = extract_numbers(self.matrix)

        # number in the middle of matrix
        n = numbers[6]
        cells = list_adj_cells(n, self.matrix)
        self.assertEqual(cells, ['.', '.', '.', '.', '.', '.','.', '.', '.', '+', '.', '.'])

        # number in the top row, left corner
        n = numbers[0]
        cells = list_adj_cells(n, self.matrix)
        self.assertEqual(cells, ['.', '.', '.', '.', '*'])

        # number in the bottom row
        n = numbers[9]
        cells = list_adj_cells(n, self.matrix)
        self.assertEqual(cells, ['*', '.', '.', '.', '.', '.', '.'])

    def test_is_part_number(self):
        numbers = extract_numbers(self.matrix)
        self.assertTrue(is_part_number(numbers[0], self.matrix))
        self.assertTrue(is_part_number(numbers[7], self.matrix))
        self.assertFalse(is_part_number(numbers[1], self.matrix))
        self.assertFalse(is_part_number(numbers[5], self.matrix))
        
        
    def test_sum_part_numbers(self):
        self.assertEqual(sum_part_numbers(self.matrix), 4361)

if __name__ == "__main__":
   unittest.main()
