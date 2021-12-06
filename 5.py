from collections import defaultdict
import sys

def clamp(x, y, z):
    return z if x > z else y if x < y else x

inp = filter(bool, map(str.strip, sys.stdin.readlines()))
lines = [
    [list(map(int, ps.split(','))) for ps in l.split(' -> ')]
    for l in inp
]

board = defaultdict(int)
overlaps = 0
for p1, p2 in lines:
    x, y = p1[0], p1[1]
    dx, dy = clamp(p2[0] - p1[0], -1, 1), clamp(p2[1] - p1[1], -1, 1)

    board[(x, y)] += 1
    if board[(x, y)] == 2:
        overlaps += 1

    while x != p2[0] or y != p2[1]:
        x += dx
        y += dy
        board[(x, y)] += 1
        if board[(x, y)] == 2:
            overlaps += 1

print(overlaps)
