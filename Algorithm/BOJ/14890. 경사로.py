N, L = list(map(int, input().split()))
road = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
slope = [[0] * N for _ in range(N)]
i = 0
while i < N:
    j, flag = 0, 0
    while j < N - 1:
        if road[i][j] == road[i][j + 1]:
            j += 1
        elif road[i][j] - road[i][j + 1] == 1:
            if j + L >= N:
                flag = 1
                break
            else:
                for k in range(j + 1, j + L):
                    if road[i][k] != road[i][k + 1]:
                        flag = 1
                        break
                if flag:
                    break
                else:
                    for k in range(j + 1, j + L + 1):
                        slope[i][k] = 1
                    j += L
        elif road[i][j] - road[i][j + 1] == -1:
            if L == 1:
                if slope[i][j] == 1:
                    flag = 1
                    break
                else:
                    j += 1
            else:
                if j + 1 - L < 0:
                    flag = 1
                    break
                else:
                    for k in range(j + 1 - L, j):
                        if road[i][k] != road[i][k + 1] or slope[i][k]:
                            flag = 1
                            break
                    if flag:
                        break
                    else:
                        j += 1
        else:
            flag = 1
            break
    if not flag:
        cnt += 1
    i += 1

slope = [[0] * N for _ in range(N)]
j = 0
while j < N:
    i, flag = 0, 0
    while i < N - 1:
        if road[i][j] == road[i + 1][j]:
            i += 1
        elif road[i][j] - road[i + 1][j] == 1:
            if i + L >= N:
                flag = 1
                break
            else:
                for k in range(i + 1, i + L):
                    if road[k][j] != road[k + 1][j]:
                        flag = 1
                        break
                if flag:
                    break
                else:
                    for k in range(i + 1, i + L + 1):
                        slope[k][j] = 1
                    i += L
        elif road[i][j] - road[i + 1][j] == -1:
            if L == 1:
                if slope[i][j] == 1:
                    flag = 1
                    break
                else:
                    i += 1
            else:
                if i + 1 - L < 0:
                    flag = 1
                    break
                else:
                    for k in range(i + 1 - L, i):
                        if road[k][j] != road[k + 1][j] or slope[k][j] or slope[k + 1][j]:
                            flag = 1
                            break
                    if flag:
                        break
                    else:
                        i += 1
        else:
            flag = 1
            break
    if not flag:
        cnt += 1
    j += 1
print(cnt)