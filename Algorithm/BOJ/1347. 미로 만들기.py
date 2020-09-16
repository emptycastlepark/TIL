di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
board = [[0] * 101 for _ in range(101)]
si, sj, ei, ej = 50, 50, 50, 50
i, j, k = 50, 50, 0
board[i][j] = '.'
N = int(input())
for com in input():
    if com == 'F':
        i += di[k]; j += dj[k]
        board[i][j] = '.'
        si, sj = min(i, si), min(j, sj)
        ei, ej = max(i, ei), max(j, ej)
    elif com == 'L':
        k = (k + 1) % 4
    else:
        k = (k + 3) % 4

board = board[si: ei + 1]
for i in range(len(board)):
    board[i] = board[i][sj: ej + 1]
    for j in range(len(board[i])):
        if not board[i][j]:
            board[i][j] = '#'

for b in board:
    print(''.join(b))