import sys

depth, pos, aim = 0, 0, 0
for cmd, amt in map(str.split, sys.stdin.readlines()):
    if cmd == "forward":
        pos += int(amt)
        depth += aim * int(amt)
    elif cmd == "down":
        aim += int(amt)
    elif cmd == "up":
        aim -= int(amt)
print(depth * pos)