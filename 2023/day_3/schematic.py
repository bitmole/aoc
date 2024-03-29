import unittest
import re

def parse_matrix(rows):
    return [[c for c in r] for r in rows]

def find_numbers(matrix):
    numbers = []
    for i, r in enumerate(matrix):
        for m in re.finditer(r'(\d+)', ''.join(r)):
            numbers.append((int(m.group(0)), m.start(), m.end(), i))
    return numbers

def filter_part_numbers(matrix):
    numbers = find_numbers(matrix)
    return [n[0] for n in numbers if is_part_number(n, matrix)]


def find_gears(matrix):
    gear_matrix = build_gear_matrix(matrix)
    # filter only valid gears with exactly 2 elements
    return [e for r in gear_matrix
              for e in r
              if e is not None and len(e)==2]

def sum_gears(matrix):
    gears = find_gears(matrix)
    return sum([g[0] * g[1] for g in gears if len(g)==2])

def build_gear_matrix(matrix):
    # init gear matrix with empty lists for part numbers in place of each "gear"
    gear_matrix = [[[] if x=='*' else None for x in r] for r in matrix]

    # populate gears with adjacent part numbers
    numbers = find_numbers(matrix)
    for n in numbers:
        gears = [c for c in list_adj_cells(n, gear_matrix) if c is not None]
        for gear in gears:
            gear.append(n[0])

    return gear_matrix

def list_adj_cells(n_rec, matrix):
    _, start, end, i = n_rec
    has_prev_row = i > 0
    has_next_row = i < len(matrix) - 1
    has_prev_col = start > 0
    has_next_col = len(matrix[i]) > end
    cells = []

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

def answers():
    input_lines = (l.strip() for l in open('input.txt').readlines())
    matrix = parse_matrix(input_lines)
    print('part numbers sum:', sum_part_numbers(matrix))
    print('gears sum:', sum_gears(matrix))
    

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

    def test_find_gears(self):
        gears = find_gears(self.matrix)
        self.assertEqual(gears, [[467, 35], [755, 598]])

    def test_sum_gears(self):
        self.assertEqual(sum_gears(self.matrix), 467835)
        
if __name__ == "__main__":
    unittest.main()
