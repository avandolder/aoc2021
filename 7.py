def cost(x, c):
    d = abs(c - x)
    return d * (d + 1) / 2

def min_fuel(crabs):
    return min(sum(cost(x, c) for c in crabs) for x in range(max(crabs)))

crabs = [int(x) for x in input().split(',')]
print(min_fuel(crabs))
