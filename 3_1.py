import sys

digits: list[int] = []
for report in filter(lambda x: x, map(str.strip, sys.stdin.readlines())):
    for i, d in enumerate(report):
        if len(digits) <= i:
            digits.append(int(d))
        else:
            digits[i] += 1 if d == "1" else -1

gamma = int(''.join(['1' if d > 0 else '0' for d in digits]), 2)
epsilon = int(''.join(['0' if d > 0 else '1' for d in digits]), 2)
print(gamma * epsilon)
