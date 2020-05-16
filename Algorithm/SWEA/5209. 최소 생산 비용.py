def f(i):
    global cost, mincost
    if i == N:
        if cost < mincost:
            mincost = cost
    for j in range(N):
        if used[j] != 1 and cost + costarr[i][j] < mincost:
            cost += costarr[i][j]; used[j] = 1
            f(i+1)
            cost -= costarr[i][j]; used[j] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    costarr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    cost, mincost = 0, 99 * N
    f(0)
    print('#{} {}'.format(tc, mincost))