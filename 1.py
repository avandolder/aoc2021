import sys
depths = [int(x) for x in sys.stdin.readlines()]
# for part 2:
depths = [sum(depths[x:x+3]) for x in range(len(depths) - 2)]
print(sum(1 if x < y else 0
          for x, y in zip(depths[:-1], depths[1:])))
