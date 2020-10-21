from itertools import combinations
import math

for tc in range(int(input())):
    N = int(input())
    city = [list(map(int, input().split())) for _ in range(N)]
    house, store = [], []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house.append((i, j))
            elif city[i][j] > 1:
                store.append((i, j))
    ans = math.inf
    for n in range(N):
        combi = list(combinations(store, n + 1))
        for com in combi:
            temp = 0
            for ci, cj in com:
                temp += city[ci][cj]
            for hi, hj in house:
                temp_dis = set()
                for ci, cj in com:
                    temp_dis.add(abs(ci - hi) + abs(cj - hj))
                temp += min(temp_dis)
                if temp > ans:
                    break
            ans = min(ans, temp)

    print('#{} {}'.format(tc + 1, ans))