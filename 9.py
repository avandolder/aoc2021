from functools import reduce
from operator import mul
import sys

def basin(i, j, seen=None):
    if seen is None:
        seen = set()
    if (i, j) in seen or i < 0 or j < 0 or i >= n or j >= m or grid[i][j] >= 9:
        return 0
    seen.add((i, j))

    return (
        1 +
        basin(i - 1, j, seen) +
        basin(i, j - 1, seen) +
        basin(i + 1, j, seen) +
        basin(i, j + 1, seen)
    )

grid = [
    [int(d) for d in line]
    for line in filter(bool, map(str.strip, sys.stdin.readlines()))
]

n, m = len(grid), len(grid[0])

low = []
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
        low += [(i, j)]

print(reduce(mul, sorted(list(map(lambda x: basin(*x), low)))[::-1][:3], 1))
