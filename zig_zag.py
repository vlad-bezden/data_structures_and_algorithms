"""Prints matrix in zig zag format"""

from pprint import pprint

ROWS = 10
COLS = 5
matrix = [[r * COLS + c for c in range(COLS)] for r in range(ROWS)]
pprint(matrix)

output = [row[::-1] if i % 2 else row for i, row in enumerate(matrix)]

pprint(output)
