N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
path = [[0] * N for _ in range(N)]
path[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
        if path[i][j]:
            ni = i + board[i][j]
            nj = j + board[i][j]
            if ni < N:
                path[ni][j] += path[i][j]
            if nj < N:
                path[i][nj] += path[i][j]
print(path[-1][-1])