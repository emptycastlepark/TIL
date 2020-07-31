from collections import deque

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs():
    global tempsum
    while border:
        i, j = border.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and checked[ni][nj] == 0:
                if L <= abs(country[i][j] - country[ni][nj]) <= R:
                    checked[ni][nj] = 1
                    border.append((ni, nj))
                    temp.append((ni, nj))
                    tempsum += country[ni][nj]

N, L, R = map(int, input().split())
country = [None] * N
for i in range(N):
    country[i] = list(map(int, input().split()))
cnt = 0
while True:
    checked = [[0] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if checked[i][j] == 0:
                checked[i][j] = 1
                border = deque([(i, j)])
                temp, tempsum = [(i, j)], country[i][j]
                bfs()
                if len(temp) != 1:
                    flag = 1
                    tempsum //= len(temp)
                    for x, y in temp:
                        country[x][y] = tempsum
    if flag:
        cnt += 1
    else:
        break
print(cnt)