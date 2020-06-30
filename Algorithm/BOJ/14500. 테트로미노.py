di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
def tetro(i, j, s, cnt):
    global maxs
    if cnt == 4:
        if s > maxs:
            maxs = s
    else:
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and checked[ni][nj] == 0:
                checked[ni][nj] = 1
                tetro(ni, nj, s + board[ni][nj], cnt + 1)
                checked[ni][nj] = 0

def rest(i, j):
    global maxs
    if i == 0:
        if j == (0 or M - 1): return
        else:
            s = board[i][j - 1] + board[i][j] + board[i][j + 1] + board[i + 1][j]
    elif i == N - 1:
        if j == (0 or M - 1): return
        else:
            s = board[i][j - 1] + board[i][j] + board[i][j + 1] + board[i - 1][j]
    else:
        if j == 0:
            s = board[i - 1][j] + board[i][j] + board[i + 1][j] + board[i][j + 1]
        elif j == M - 1:
            s = board[i - 1][j] + board[i][j] + board[i + 1][j] + board[i][j - 1]
        else:
            temp = set()
            temp.add(board[i][j - 1] + board[i][j] + board[i][j + 1] + board[i + 1][j])
            temp.add(board[i][j - 1] + board[i][j] + board[i][j + 1] + board[i - 1][j])
            temp.add(board[i - 1][j] + board[i][j] + board[i + 1][j] + board[i][j + 1])
            temp.add(board[i - 1][j] + board[i][j] + board[i + 1][j] + board[i][j - 1])
            s = max(temp)
    if s > maxs:
        maxs = s

N, M = map(int, input().split())
board = [None] * N
for i in range(N):
    board[i] = list(map(int, input().split()))
maxs = 0
checked = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        checked[i][j] = 1
        tetro(i, j, board[i][j], 1)
        checked[i][j] = 0
        rest(i, j)
print(maxs)