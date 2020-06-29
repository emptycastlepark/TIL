dice = [0] * 6

def move(x, y, c):
    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5] = board[x][y]
        board[x][y] = 0
    print(dice[2])

N, M, x, y, K = map(int, input().split())
board = [None] * N
for i in range(N):
    board[i] = list(map(int, input().split()))
command = list(map(int, input().split()))

for c in command:
    if c == 1:
        if y + 1 < M:
            y += 1
            dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
            move(x, y, c)
    elif c == 2:
        if 0 <= y - 1:
            y -= 1
            dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
            move(x, y, c)
    elif c == 3:
        if 0 <= x - 1:
            x -= 1
            dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
            move(x, y, c)
    else:
        if x + 1 < N:
            x += 1
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
            move(x, y, c)