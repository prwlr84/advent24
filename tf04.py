from math import prod
from re import findall, sub
from tf04i import inputString

# 1
grid = [list(line) for line in inputString.split('\n')]
word = 'XMAS'
rows, cols = len(grid), len(grid[0])
word_len = len(word)
directions = [
    (0, 1),  # → right
    (0, -1),  # ← left
    (1, 0),  # ↓ down
    (-1, 0),  # ↑ up
    (1, 1),  # ↘ down-right
    (-1, -1),  # ↖ up-left
    (1, -1),  # ↙ down-left
    (-1, 1),  # ↗ up-right
]

matches = []

for r in range(rows):
    for c in range(cols):
        for dr, dc in directions:
            positions = []
            for i in range(len(word)):
                nr, nc = r + dr * i, c + dc * i
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == word[i]:
                    positions.append((nr, nc))
                else:
                    break
            if len(positions) == word_len:
                matches.append(positions)

print('First', len(matches))


# 2
def is_a_match(diagonal: str) -> bool:
    return diagonal == 'MAS' or diagonal == 'SAM'

count = 0

# Loop over each line except first and last (because we look above and below)
for row in range(1, len(grid) - 1):
    line = grid[row]

    for col, char in enumerate(line):
        if char != 'A':
            continue

        try:
            left_diag = grid[row - 1][col - 1] + char + grid[row + 1][col + 1]
            right_diag = grid[row + 1][col - 1] + char + grid[row - 1][col + 1]

            if is_a_match(left_diag) and is_a_match(right_diag):
                count += 1

        except IndexError:
            continue

print('Second:', count)
