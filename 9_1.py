import sys

grid = [
    [int(d) for d in line]
    for line in filter(bool, map(str.strip, sys.stdin.readlines()))
]


n, m = len(grid), len(grid[0])

low = 0
for i, row in enumerate(grid):
    for j, level in enumerate(row):
        if i - 1 >= 0 and level >= grid[i - 1][j]:
            continue
        if j - 1 >= 0 and level >= grid[i][j - 1]:
            continue
        if i + 1 < n and level >= grid[i + 1][j]:
            continue
        if j + 1 < m and level >= grid[i][j + 1]:
            continue
        low += level + 1

print(low)
