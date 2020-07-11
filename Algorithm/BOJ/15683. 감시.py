def check(dir, i, j, a):
    for d in dir:
        # 위
        if d == 0:
            for k in range(i - 1, -1, -1):
                if room[k][j] == 6:
                    break
                elif room[k][j] in range(1, 6):
                    continue
                else:
                    room[k][j] += a
        # 오른
        elif d == 1:
            for k in range(j + 1, M):
                if room[i][k] == 6:
                    break
                elif room[i][k] in range(1, 6):
                    continue
                else:
                    room[i][k] += a
        # 아래
        elif d == 2:
            for k in range(i + 1, N):
                if room[k][j] == 6:
                    break
                elif room[k][j] in range(1, 6):
                    continue
                else:
                    room[k][j] += a
        # 왼
        else:
            for k in range(j - 1, -1, -1):
                if room[i][k] == 6:
                    break
                elif room[i][k] in range(1, 6):
                    continue
                else:
                    room[i][k] += a

def watch(cctv, cnt):
    global ans
    if cnt == len(cctv):
        temp = 0
        for r in room:
            temp += r.count(0)
        ans = min(ans, temp)
        return

    cam = cctv[cnt]
    i, j, num = cam
    # 1번 카메라
    if num == 1:
        for dir in range(4):
            check([dir], i, j, -1)
            watch(cctv, cnt + 1)
            check([dir], i, j, 1)
    # 2번 카메라
    elif num == 2:
        for dir in ([[0, 2], [1, 3]]):
            check(dir, i, j, -1)
            watch(cctv, cnt + 1)
            check(dir, i, j, 1)
    # 3번 카메라
    elif num == 3:
        for dir in([[0, 1], [1, 2], [2, 3], [3, 0]]):
            check(dir, i, j, -1)
            watch(cctv, cnt + 1)
            check(dir, i, j, 1)
    # 4번 카메라
    elif num == 4:
        for dir in ([[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]):
            check(dir, i, j, -1)
            watch(cctv, cnt + 1)
            check(dir, i, j, 1)
    # 5번 카메라
    else:
        check([0, 1, 2, 3], i, j, -1)
        watch(cctv, cnt + 1)
        check([0, 1, 2, 3], i, j, 1)

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if room[i][j] in range(1, 6):
            cctv.append([i, j, room[i][j]])
ans = N * M
watch(cctv, 0)
print(ans)