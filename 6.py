from functools import cache

@cache
def fish_count(day, days_til_spawn):
    if day <= 0:
        return 1
    return fish_count(day - days_til_spawn, 9) + fish_count(day - days_til_spawn, 7)

def fish_count2(days, fishes):
    fs = [0] * 9
    ts = [0] * 9
    for f in fishes:
        fs[f] += 1
    for _ in range(days):
        for i, f in enumerate(fs[1:]):
            ts[i] = f
        ts[8] = fs[0]
        ts[6] += fs[0]
        fs, ts = ts, fs
    return sum(fs)

fish = [int(x) for x in input().strip().split(',')]
print(sum(fish_count(256, f) for f in fish) // 2)
print(fish_count2(256, fish))
