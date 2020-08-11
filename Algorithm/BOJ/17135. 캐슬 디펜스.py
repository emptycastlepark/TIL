from itertools import combinations
from copy import deepcopy
from collections import deque

di, dj = [0, -1, 0], [-1, 0, 1]

def shoot(archer, board):
    cnt = 0
    for _ in range(N):
        attack = set()
        for a in archer:
            visited = [[0] * M for _ in range(N)]
            queue = deque([(N - 1, a)])
            while queue:
                i, j = queue.popleft()
                visited[i][j] = 1
                if abs((N - i) + (a - j)) > D:
                    break
                if board[i][j]:
                    attack.add((i, j))
                    break
                for k in range(3):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni and 0 <= nj < M and visited[ni][nj] == 0:
                        queue.append((ni, nj))
        cnt += len(attack)
        for ti, tj in attack:
            board[ti][tj] = 0
        board.pop()
        board.insert(0, [0] * M)
    return cnt

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
archer = list(range(M))
archercase = list(combinations(archer, 3))
ans = 0
for ac in archercase:
    temp_board = deepcopy(board)
    ans = max(ans, shoot(ac, temp_board))
print(ans)