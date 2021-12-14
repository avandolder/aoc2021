from itertools import count
import sys

def step(g):
    for i in range(10):
        for j in range(10):
            g[i][j] += 1

    for i in range(10):
        for j in range(10):
            if g[i][j] > 9:
                flash(g, i, j)

def flash(g, i, j):
    g[i][j] = 0

    for k in range(-1, 2):
        for l in range(-1, 2):
            x, y = i + k, j + l
            if x < 0 or y < 0 or x >= 10 or y >= 10:
                continue
            if g[x][y] > 0:
                g[x][y] += 1
                if g[x][y] > 9:
                    flash(g, x, y)

grid = [
    [int(d) for d in line]
    for line in filter(bool, map(str.strip, sys.stdin.readlines()))
]

for x in count():
    step(grid)
    if all(grid[i][j] == 0 for i in range(10) for j in range(10)):
        print(x + 1)
        break
