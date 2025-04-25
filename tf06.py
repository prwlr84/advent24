from tf06i import input_string

grid = [list(line) for line in input_string.split('\n')]
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col == '^':
            start = (y, x)
            break

def rotate_grid(g):
    return [list(r) for r in zip(*g)][::-1]


def count_steps():
    self_grid = grid
    pos = start
    current_pos = start
    while current_pos[0] >= 0:
        if self_grid[current_pos[0]][pos[1]] ==  '#':
            self_grid = rotate_grid(self_grid)
            pos = (len(grid[0]) - 1 - current_pos[1], current_pos[0] + 1)
            current_pos = pos
        else:
            self_grid[current_pos[0]][current_pos[1]] = 'X'
            current_pos = (current_pos[0] - 1, current_pos[1])
            continue

    return sum(r.count('X') for r in self_grid)


print('First:', count_steps())