from tf05i import inputString
from collections import defaultdict, deque

# 1
rules_block, lines_block = inputString.strip().split('\n\n')
rules = [tuple(map(int, r.split('|'))) for r in rules_block.strip().split('\n')]
lines = [list(map(int, line.split(','))) for line in lines_block.strip().split('\n')]


def is_valid(series):
    pos = {val: i for i, val in enumerate(series)}
    return all(pos[a] < pos[b] for a, b in rules if a in pos and b in pos)


valid_lines = []
invalid_lines = []

for line in lines:
    if is_valid(line):
        valid_lines.append(line)
    else:
        invalid_lines.append(line)

middle_values = [line[len(line) // 2] for line in valid_lines]
middle_sum = sum(middle_values)
print('First', middle_sum)


# 2
def sort_to_comply(elements):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    element_set = set(elements)

    for before, after in rules:
        if before in element_set and after in element_set:
            graph[before].append(after)
            indegree[after] += 1
            if before not in indegree:
                indegree[before] = 0

    queue = deque(sorted([n for n in element_set if indegree[n] == 0]))
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in sorted(graph[current]):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result


fixed_invalid_lines = [sort_to_comply(line) for line in invalid_lines]
middle_values_fixed = [line[len(line) // 2] for line in fixed_invalid_lines]
middle_sum_fixed = sum(middle_values_fixed)
print('Second', middle_sum_fixed)
