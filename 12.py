from collections import defaultdict
import sys

def paths(g, v, t=False, seen=None):
    if seen is None:
        seen = {v}
    if v == 'end':
        return 1

    ps = 0
    for u in g[v]:
        if u not in seen:
            if u.lower() == u:
                ps += paths(g, u, t, seen | {u})
            else:
                ps += paths(g, u, t, seen)
        elif u != 'start' and u.lower() == u and not t:
            ps += paths(g, u, True, seen)
    return ps

g = defaultdict(set)
for line in filter(bool, map(str.strip, sys.stdin.readlines())):
    u, v = line.split('-')
    g[u].add(v)
    g[v].add(u)

print(paths(g, 'start'))
