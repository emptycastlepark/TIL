N = int(input())
board = [[0] * 101 for _ in range(101)]
dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    board[x][y] = 1
    curve = [d]
    for _ in range(g):
        curve += [(i + 1) % 4 for i in curve[::-1]]
    for cur in curve:
        x += dx[cur]; y += dy[cur]
        board[x][y] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            if board[i][j + 1] == board[i + 1][j + 1] == board[i + 1][j] == 1:
                cnt += 1
print(cnt)