import copy

def solution(road):
    cnt = 0
    slope = [[0] * N for _ in range(N)]
    for i in range(N):
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
    return cnt

N, L = list(map(int, input().split()))
road = [list(map(int, input().split())) for _ in range(N)]
rotate_road = copy.deepcopy(road)
for i in range(N):
    for j in range(N):
        rotate_road[j][i] = road[i][N - 1 - j]
print(solution(road) + solution(rotate_road))