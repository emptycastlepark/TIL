from itertools import combinations

N = int(input())
people = list(range(N))
team = list(combinations(people, N // 2))
ability = [None] * N
for i in range(N):
    ability[i] = list(map(int, input().split()))
minans = 20000
for i in range(len(team) // 2):
    start = list(team[i])
    link = []
    for p in people:
        if p not in start:
            link.append(p)
    s1, s2 = 0, 0
    for t1 in range(N // 2):
        for t2 in range(t1 + 1, N // 2):
            s1 += (ability[start[t1]][start[t2]] + ability[start[t2]][start[t1]])
            s2 += (ability[link[t1]][link[t2]] + ability[link[t2]][link[t1]])
    if abs(s1 - s2) < minans:
        minans = abs(s1 - s2)
print(minans)