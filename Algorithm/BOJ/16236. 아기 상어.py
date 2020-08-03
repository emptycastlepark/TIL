from collections import deque

di, dj = [0, -1, 0, 1], [-1, 0, 1, 0]

def bfs(si, sj):
    queue, visited = deque([(si, sj)]), deque([(si, sj)])
    ans, time, cnt, shark = 0, 0, 0, 2
    flag = False

    while queue:
        lenq = len(queue)
        queue = deque(sorted(queue))
        for _ in range(lenq):
            i, j = queue.popleft()
            if space[i][j] != 0 and space[i][j] < shark:
                cnt += 1
                space[i][j] = 0
                if cnt == shark:
                    shark += 1
                    cnt = 0
                queue, visited = deque(), deque([(i, j)])
                flag = True
                ans = time
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
                    if space[ni][nj] <= shark:
                        queue.append((ni, nj))
                        visited.append((ni, nj))
            if flag:
                flag = False
                break
        time += 1
    return ans

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
flag, si, sj = False, None, None
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            space[i][j] = 0
            si, sj = i, j
            flag = True
            break
    if flag:
        break
print(bfs(si, sj))