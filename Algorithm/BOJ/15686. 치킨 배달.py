import math
from itertools import combinations

N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]
ans = math.inf
home, store = [], []
for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            home.append((i, j))
        elif town[i][j] == 2:
            store.append((i, j))
combi = list(combinations(store, M))
for com in combi:
    distance = 0
    for h in home:
        temp = set()
        for c in com:
            temp.add(abs(h[0] - c[0]) + abs(h[1] - c[1]))
        distance += min(temp)
    ans = min(ans, distance)
print(ans)