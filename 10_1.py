import sys

def score(line):
    stack = []
    for c in line:
        if c in openers:
            stack.append(openers[c])
        elif stack.pop() != c:
            return scores[c]
    return 0

openers = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

lines = list(filter(bool, map(str.strip, sys.stdin.readlines())))
print(sum(score(line) for line in lines))
