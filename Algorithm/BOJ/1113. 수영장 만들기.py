from collections import deque

di, dj = [0, -1, 0, 1], [-1, 0, 1, 0]

def bfs(i, j, h):
    global ans
    q = deque(); q.append([i, j])
    pool = deque(); pool.append([i, j])
    flag = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if not checked[ni][nj]:
                    checked[ni][nj] = 1
                    if land[ni][nj] < h:
                        q.append([ni, nj]); pool.append([ni, nj])
            else:
                flag = 1
    if flag:
        return
    for wi, wj in pool:
        ans += (h - land[wi][wj])
        land[wi][wj] = h

N, M = map(int, input().split())
land = [None] * N
maxh = 0
for i in range(N):
    land[i] = list(map(int, input()))
    maxh = max(maxh, max(land[i]))
ans = 0
for h in range(2, maxh + 1):
    checked = [[0] * M for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if land[i][j] < h and not checked[i][j]:
                checked[i][j] = 1
                bfs(i, j, h)
print(ans)