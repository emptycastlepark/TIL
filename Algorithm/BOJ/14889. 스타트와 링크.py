from itertools import combinations

N = int(input())
people = list(range(N))
team = list(combinations(people, N // 2))
ability = [list(map(int, input().split())) for _ in range(N)]
ans = 20000
for i in range(len(team) // 2):
    start = list(team[i])
    link = list(team[len(team) - 1 - i])
    s1, s2 = 0, 0
    for t1 in range(N // 2):
        for t2 in range(t1 + 1, N // 2):
            s1 += (ability[start[t1]][start[t2]] + ability[start[t2]][start[t1]])
            s2 += (ability[link[t1]][link[t2]] + ability[link[t2]][link[t1]])
    if s1 == s2:
        ans = 0
        break
    if abs(s1 - s2) < ans:
        ans = abs(s1 - s2)
print(ans)