from collections import deque

def rotate_cnt(d, nd, c):
    if d in (1, 2):
        if nd in (1, 2):
            if d != nd:
                c += 2
        else:
            c += 1
    else:
        if nd in (3, 4):
            if d != nd:
                c += 2
        else:
            c += 1
    return c

dir = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

M, N = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(M)]
si, sj, sd = map(int, input().split())
ei, ej, ed = map(int, input().split())
si -= 1; sj -= 1; ei -= 1; ej -= 1

pushed = [[[False for _ in range(5)] for _ in range(N)] for _ in range(M)]
queue = deque(); queue.append((si, sj, sd, 0))
pushed[si][sj][sd] = True
while queue:
    i, j, d, c = queue.popleft()
    if i == ei and j == ej:
        break
    # 명령 1: 이동
    ni, nj = i, j
    for _ in range(3):
        ni += dir[d][0]; nj += dir[d][1]
        if 0 <= ni < M and 0 <= nj < N:
            if pushed[ni][nj][d]:
                continue
            if not factory[ni][nj]:
                queue.append((ni, nj, d, c + 1))
                pushed[ni][nj][d] = True
            else:
                break
        else:
            break
    # 명령 2: 회전
    for nd in range(1, 5):
        if not pushed[i][j][nd]:
            queue.append((i, j, nd, rotate_cnt(d, nd, c)))
            pushed[i][j][nd] = True

print(rotate_cnt(d, ed, c))