from collections import deque

dx, dy = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
N, M, K = map(int, input().split())
soil = [[5] * N for _ in range(N)]
A = [None] * N
for i in range(N):
    A[i] = list(map(int, input().split()))
tree = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1] = deque([z])
year = 0
while year < K:
    treexy = deque()
    # 봄
    for x in range(N):
        for y in range(N):
            if tree[x][y]:
                treexy.append((x, y))
                temp = deque(tree[x][y])
                tree[x][y] = deque()
                while temp:
                    t = temp.popleft()
                    if t > soil[x][y]:
                        temp.appendleft(t)
                        break
                    soil[x][y] -= t
                    tree[x][y].append(t + 1)
                if temp:
                    tree[x][y].append(temp)
    # 여름
    for x, y in treexy:
        if len(tree[x][y]) > 0 and type(tree[x][y][-1]) != int:
            for t in tree[x][y][-1]:
                soil[x][y] += t // 2
            tree[x][y].pop()
    # 가을
    for x, y in treexy:
        for t in tree[x][y]:
            if t % 5 == 0:
                for k in range(8):
                    kx, ky = x + dx[k], y + dy[k]
                    if 0 <= kx < N and 0 <= ky < N:
                        tree[kx][ky].appendleft(1)
    # 겨울
    for x in range(N):
        for y in range(N):
            soil[x][y] += A[x][y]
    year += 1

ans = 0
for x in range(N):
    for y in range(N):
        if tree[x][y]:
            ans += len(tree[x][y])
print(ans)