N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
for r in range(N - 1):
    maze[r + 1][0] += maze[r][0]
for c in range(M - 1):
    maze[0][c + 1] += maze[0][c]
for r in range(1, N):
    for c in range(1, M):
        maze[r][c] += max(maze[r - 1][c - 1], maze[r - 1][c], maze[r][c - 1])
print(maze[-1][-1])