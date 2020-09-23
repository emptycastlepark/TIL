from itertools import combinations
from collections import deque

student = list(input() for _ in range(5))
ans, scnt = 0, 0
for s in student:
    scnt += s.count('S')
if scnt >= 4:
    cases = list(combinations(list(range(25)), 7))
    able_case = []
    for case in cases:
        flag, scnt = 0, 0
        for c in case:
            i, j = divmod(c, 5)
            if student[i][j] == 'S':
                scnt += 1
                if scnt == 4:
                    flag = 1
                    break
        if flag:
            able_case.append(list(case))

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    if len(able_case) > 0:
        for a_c in able_case:
            temp = 0
            queue = deque(); queue.append(a_c[0])
            checked = [[0] * 5 for _ in range(5)]
            checked[a_c[0] // 5][a_c[0] % 5] = 1
            while queue:
                temp += 1
                i, j = divmod(queue.popleft(), 5)
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    for p in range(7):
                        pi, pj = divmod(a_c[p], 5)
                        if ni == pi and nj == pj and not checked[ni][nj]:
                            checked[ni][nj] = 1
                            queue.append(a_c[p])
            if temp == 7:
                ans += 1

print(ans)