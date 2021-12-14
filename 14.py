from collections import Counter
from functools import cache
import sys

@cache
def count(pair, steps):
    if steps == 0 or pair not in rules:
        return Counter(pair)
    return count(pair[0] + rules[pair], steps - 1) + count(rules[pair] + pair[1], steps - 1)

template = input()

rules = {}
for line in filter(bool, map(str.strip, sys.stdin.readlines())):
    x, y = line.split(' -> ')
    rules[x] = y

c = Counter()
for i in range(len(template) - 1):
    c += count(template[i:i+2], 40)

print((max(c.values()) - min(c.values())) / 2)
