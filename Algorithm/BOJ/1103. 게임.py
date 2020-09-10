# dfs + memoization

from collections import deque

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def move(i, j, cnt):
    global ans
    if ans == -1:
        return
    ans = max(cnt, ans)
    visited.append((i, j))
    memo[i][j] = cnt
    for k in range(4):
        ni, nj = i + di[k] * int(board[i][j]), j + dj[k] * int(board[i][j])
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 'H':
            if (ni, nj) in visited:
                ans = -1
                return
            if cnt >= memo[ni][nj]:
                move(ni, nj, cnt + 1)
    visited.pop()

N, M = map(int, input().split())
board = [None] * N
for i in range(N):
    board[i] = list(input())
visited = deque()
memo = [[0] * M for _ in range(N)]
ans = 0
move(0, 0, 1)
print(ans)



# # dfs. 시간초과

# from collections import deque
#
# di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
#
# def move(i, j, cnt):
#     global ans
#     # 무한
#     if ans == -1:
#         return
#     # 인덱스 벗어나면
#     if 0 > i or i >= N or 0 > j or j >= M:
#         return
#     # 구멍에 빠지면
#     elif board[i][j] == 'H':
#         return
#     else:
#         if (i, j) in visited:
#             ans = -1
#             return
#         else:
#             visited.append((i, j))
#             ans = max(ans, cnt)
#             num = board[i][j]
#             for k in range(4):
#                 ni, nj = i + di[k] * int(num), j + dj[k] * int(num)
#                 move(ni, nj, cnt + 1)
#             visited.pop()
#
#
# N, M = map(int, input().split())
# board = [None] * N
# for i in range(N):
#     board[i] = list(input())
# visited = deque()
# ans = 0
# move(0, 0, 1)
# print(ans)