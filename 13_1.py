import sys

def fold(dots, axis, dr):
    for d in list(filter(lambda d: d[dr] > axis, dots)):
        dots.remove(d)
        newd = list(d)
        newd[dr] = axis - (d[dr] - axis)
        dots.add(tuple(newd))

lines = map(str.strip, sys.stdin.readlines())
dots = set()
for line in lines:
    if not line:
        break
    x, y = list(map(int, line.split(',')))
    dots.add((x, y))

for line in lines:
    if line.startswith('fold along '):
        f = line[11:]
        break

dr = 0 if f[0] == 'x' else 1
axis = int(f[2:])
fold(dots, axis, dr)
print(len(dots))
