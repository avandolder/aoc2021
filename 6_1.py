fish = [int(x) for x in input().strip().split(',')]
print(fish)

for _ in range(256):
    temp = []
    for f in fish:
        if f == 0:
            temp += [6, 8]
        else:
            temp += [f - 1]
    fish = temp

print(len(fish))
