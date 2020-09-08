def mafia(n, cnt):
    global ans, flag
    if killed[num]:
        ans = max(ans, cnt)
        return
    if n == 1:
        ans = max(ans, cnt)
        flag = 1
        return
    # 낮
    if n % 2:
        max_sin = sin.index(max(sin))
        temp1 = sin[max_sin]
        killed[max_sin] = 1
        sin[max_sin] -= temp1
        mafia(n - 1, cnt)
        killed[max_sin] = 0
        sin[max_sin] += temp1
    # 밤
    else:
        for i in range(N):
            if i != num and killed[i] == 0:
                temp2 = sin[i]
                killed[i] = 1
                sin[i] -= temp2
                for j in range(N):
                    if sin[j]:
                        sin[j] += R[i][j]
                mafia(n - 1, cnt + 1)
                if flag:
                    return
                killed[i] = 0
                for j in range(N):
                    if sin[j]:
                        sin[j] -= R[i][j]
                sin[i] += temp2

N = int(input())
sin = list(map(int, input().split()))
R = [list(map(int, input().split())) for _ in range(N)]
num = int(input())

killed = [0] * N
ans, flag = 0, 0
mafia(N, 0)
print(ans)