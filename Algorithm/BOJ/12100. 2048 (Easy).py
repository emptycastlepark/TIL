from copy import deepcopy

def move(board, d):
    b = deepcopy(board)
    if d == 'up':
        checked = [[0] * N for _ in range(N)]
        for j in range(N):
            for i in range(N):
                if b[i][j] != 0:
                    while 0 <= i - 1 < N:
                        if b[i - 1][j] == b[i][j] and checked[i - 1][j] == 0 and checked[i][j] == 0:
                            b[i - 1][j] += b[i][j]
                            checked[i - 1][j] = 1
                            b[i][j] = 0
                            break
                        else:
                            if b[i - 1][j] == 0:
                                b[i - 1][j] = b[i][j]
                                b[i][j] = 0
                        i -= 1
    elif d == 'down':
        checked = [[0] * N for _ in range(N)]
        for j in range(N):
            for i in range(N - 1, -1, -1):
                if b[i][j] != 0:
                    while 0 <= i + 1 < N:
                        if b[i + 1][j] == b[i][j] and checked[i + 1][j] == 0 and checked[i][j] == 0:
                            b[i + 1][j] += b[i][j]
                            checked[i + 1][j] = 1
                            b[i][j] = 0
                            break
                        else:
                            if b[i + 1][j] == 0:
                                b[i + 1][j] = b[i][j]
                                b[i][j] = 0
                        i += 1
    elif d == 'left':
        checked = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if b[i][j] != 0:
                    while 0 <= j - 1 < N:
                        if b[i][j - 1] == b[i][j] and checked[i][j - 1] == 0 and checked[i][j] == 0:
                            b[i][j - 1] += b[i][j]
                            checked[i][j - 1] = 1
                            b[i][j] = 0
                            break
                        else:
                            if b[i][j - 1] == 0:
                                b[i][j - 1] = b[i][j]
                                b[i][j] = 0
                        j -= 1
    else:
        checked = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if b[i][j] != 0:
                    while 0 <= j + 1 < N:
                        if b[i][j + 1] == b[i][j] and checked[i][j + 1] == 0 and checked[i][j] == 0:
                            b[i][j + 1] += b[i][j]
                            checked[i][j + 1] = 1
                            b[i][j] = 0
                            break
                        else:
                            if b[i][j + 1] == 0:
                                b[i][j + 1] = b[i][j]
                                b[i][j] = 0
                        j += 1
    return b

def solution(cnt, board):
    global maxnum
    if cnt == 5:
        maxnum = max(maxnum, max(max(i) for i in board))
        return
    for d in direction:
        solution(cnt + 1, move(board, d))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
direction = ['up', 'down', 'left', 'right']
maxnum = 0
solution(0, board)
print(maxnum)