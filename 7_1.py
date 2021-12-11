def min_fuel(crabs):
    return min(sum(abs(c - x) for c in crabs) for x in range(max(crabs)))

crabs = [int(x) for x in input().split(',')]
print(min_fuel(crabs))
