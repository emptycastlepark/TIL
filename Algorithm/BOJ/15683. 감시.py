def check(dir, i, j, a):
    way = [range(i - 1, -1, -1), range(j + 1, M), range(i + 1, N), range(j - 1, -1, -1)]
    for d in dir:
        if d in [0, 2]:
            for k in way[d]:
                if room[k][j] == 6:
                    break
                elif room[k][j] in range(1, 6):
                    continue
                else:
                    room[k][j] += a
        else:
            for k in way[d]:
                if room[i][k] == 6:
                    break
                elif room[i][k] in range(1, 6):
                    continue
                else:
                    room[i][k] += a

def watch(cnt):
    global ans
    if cnt == len(cctv):
        temp = 0
        for r in room:
            temp += r.count(0)
        ans = min(ans, temp)
        return
    cam = cctv[cnt]
    i, j, num = cam
    for dir in direction[num - 1]:
        check(dir, i, j, -1)
        watch(cnt + 1)
        check(dir, i, j, 1)

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if room[i][j] in range(1, 6):
            cctv.append([i, j, room[i][j]])
direction = [[[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]],
             [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]
ans = N * M
watch(0)
print(ans)