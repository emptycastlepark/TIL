def f(i, cnt):
    global mincnt
    if i == N:
        if cnt < mincnt:
            mincnt = cnt
    for j in range(i+charge[i], i, -1):
        if j <= N and cnt < mincnt:
            if j == N:
                f(j, cnt)
            else:
                f(j, cnt+1)

for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    N = arr[0]; charge = [0] * (N+1)
    for i in range(1, N):
        charge[i] = arr[i]
    mincnt = N-1
    f(1, 0)
    print('#{} {}'.format(tc, mincnt))