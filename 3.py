from operator import eq, ne
import sys

def digit_count(report):
    digits = [0] * n
    for line in report:
        for i, d in enumerate(line):
            digits[i] += 1 if d == "1" else -1
    return ["1" if d >= 0 else "0" for d in digits]

def rating(report, op):
    for i in range(n):
        digits = digit_count(report)
        report = [l for l in report if op(l[i], digits[i])]
        if len(report) == 1:
            break
    return int(''.join(report), 2)

report = list(filter(bool, map(str.strip, sys.stdin.readlines())))
n = len(report[0])

oxygen = rating(report, eq)
co2 = rating(report,  ne)
print(oxygen * co2)
