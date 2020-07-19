def solution(x, cnt):
    global ans
    flag = 1
    for sj in range(N):
        j = sj
        for i in range(H):
            if ladder[i][j]:
                j += 1
            elif j > 0 and ladder[i][j - 1]:
                j -= 1
        if sj != j:
            flag = 0
            break
    if flag:
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return

    for i in range(x, H):
        for j in range(N - 1):
            if not ladder[i][j] and not ladder[i][j + 1]:
                ladder[i][j] = 1
                solution(i, cnt + 1)
                ladder[i][j] = 0

N, M, H = map(int, input().split())
ladder = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    ladder[a][b] = 1
if M == 0:
    print(0)
else:
    ans = 4
    solution(0, 0)
    if ans > 3:
        print(-1)
    else:
        print(ans)