from collections import Counter
import sys

template = input()

print(template)

rules = {}
for line in filter(bool, map(str.strip, sys.stdin.readlines())):
    x, y = line.split(' -> ')
    rules[x] = y

print(rules)

for _ in range(10):
    new = [template[0]]
    for x, y in zip(template, template[1:]):
        pair = x + y
        if pair in rules:
            new += [rules[pair], pair[1]]
        else:
            new += [pair[1]]
    template = new

c = Counter(template)
print(max(c.values()) - min(c.values()))
