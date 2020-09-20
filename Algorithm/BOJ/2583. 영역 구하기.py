import sys
sys.setrecursionlimit(10**6)

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(i, j):
    global cnt
    cnt += 1
    board[i][j] = 1

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not board[ni][nj]:
            dfs(ni, nj)
    else:
        return

M, N, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
for _ in range(K):
    si, sj, ei, ej = map(int, input().split())
    for i in range(si, ei):
        for j in range(sj, ej):
            board[i][j] = 1
ans = []
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

print(len(ans))
ans.sort()
for a in ans:
    print(a, end = ' ')