from functools import reduce
import sys

def score(line):
    stack = []
    for c in line:
        if c in openers:
            stack.append(openers[c])
        elif stack.pop() != c:
            return -1
    return reduce(lambda x, y: x*5 + scores[y], reversed(stack), 0)

openers = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

lines = list(filter(bool, map(str.strip, sys.stdin.readlines())))
scores = list(filter(lambda x: x >= 0, sorted(score(line) for line in lines)))
print(scores[len(scores) // 2])
