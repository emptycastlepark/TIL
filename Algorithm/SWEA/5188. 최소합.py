# 재귀
di, dj = [0, 1], [1, 0]
def f(i, j):
    global cnt, answer
    if i == N-1 and j == N-1:
        if cnt < answer:
            answer = cnt
    else:
        for k in range(2):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and checked[ni][nj] != 1 and cnt + arr[ni][nj] < answer:
                checked[ni][nj] = 1
                cnt += arr[ni][nj]
                f(ni, nj)
                checked[ni][nj] = 0
                cnt -= arr[ni][nj]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    checked = [[0]*N for _ in range(N)]; checked[0][0] = 1
    cnt, answer = arr[0][0], 10 * (N**2)
    f(0, 0)
    print('#{} {}'.format(tc, answer))

# DP
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A = [list(map(int,input().split())) for _ in range(N)]
    d= [[0]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        d[i][0] = N*10
        d[0][i] = N*10
    for i in range(1, N+1):
        for j in range(1, N+1):
            d[1][1] = A[0][0]
            d[i][j] = min(d[i][j-1],d[i-1][j])+A[i-1][j-1]
    print('#{} {}'.format(tc, d[N][N]))