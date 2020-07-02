import copy

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
N, M = map(int, input().split())
lab = [None] * N
for i in range(N):
    lab[i] = list(map(int, input().split()))
answer = 0
space, virus = [], []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            space.append([i, j])
        elif lab[i][j] == 2:
            virus.append([i, j])
for i in range(len(space) - 2):
    for j in range(i + 1, len(space) - 1):
        for k in range(j + 1, len(space)):
            copy_lab = copy.deepcopy(lab)
            copy_lab[space[i][0]][space[i][1]] = 1
            copy_lab[space[j][0]][space[j][1]] = 1
            copy_lab[space[k][0]][space[k][1]] = 1
            copy_virus = copy.deepcopy(virus)
            while copy_virus:
                x, y = copy_virus.pop(0)
                for d in range(4):
                    xi, yj = x + di[d], y + dj[d]
                    if 0 <= xi < N and 0 <= yj < M:
                        if copy_lab[xi][yj] == 0:
                            copy_lab[xi][yj] = 2
                            copy_virus.append([xi, yj])
            safecnt = 0
            for l in copy_lab:
                safecnt += l.count(0)
            if safecnt > answer:
                answer = safecnt
print(answer)