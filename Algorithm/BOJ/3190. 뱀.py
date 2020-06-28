di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 'a'

L = int(input())
move = [[0, 0]] * L
for l in range(L):
    s, w = input().split()
    move[l] = [int(s), w]
move.append([10000, 'fin'])

hi, hj = 0, 0
board[hi][hj] = 's'
snake = [(hi, hj)]
time, d, sec0 = 0, 0, 0

while move:
    flag = 0
    sec, way = move.pop(0)
    for _ in range(sec - sec0):
        time += 1
        hi += di[d]; hj += dj[d]
        if 0 <= hi < N and 0 <= hj < N and board[hi][hj] != 's':
            if board[hi][hj] != 'a':
                ti, tj = snake.pop(0)
                board[ti][tj] = 0
            board[hi][hj] = 's'
            snake.append((hi, hj))
        else:
            flag = 1; break
    if flag: break
    sec0 = sec
    if way == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4

print(time)