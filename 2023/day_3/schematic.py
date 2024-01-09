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

def find_numbers(matrix):
    numbers = []
    for i, r in enumerate(matrix):
        for m in re.finditer(r'(\d+)', ''.join(r)):
            numbers.append((int(m.group(0)), m.start(), m.end(), i))
    return numbers

def filter_part_numbers(matrix):
    numbers = find_numbers(matrix)
    return [val for (val, start, end, i) in numbers if is_part_number((start, end, i), matrix)]

def list_adj_cells(n_rec, matrix):
    cells = []
    start, end, i = n_rec
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
    return sum(filter_part_numbers(matrix))

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

    def test_extract_part_numbers(self):
        part_numbers = filter_part_numbers(self.matrix)
        for n in part_numbers:
            self.assertTrue(n in [467, 35, 633, 617, 592, 755, 664, 598])
            self.assertFalse(n in [114, 58])

    def test_sum_part_numbers(self):
        self.assertEqual(sum_part_numbers(self.matrix), 4361)

if __name__ == "__main__":
   unittest.main()
