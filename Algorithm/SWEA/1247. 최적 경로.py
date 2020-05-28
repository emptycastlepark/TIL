def f(x, y):
    global dis, mindis
    if 0 not in visited:
        dis += abs(xyli[2]-x) + abs(xyli[3]-y)
        if dis < mindis:
            mindis = dis
        dis -= abs(xyli[2]-x) + abs(xyli[3]-y)
    else:
        for i in range(N):
            if visited[i] == 0 and (dis + abs(x - customer[i][0]) + abs(y - customer[i][1])) < mindis:
                visited[i] = 1
                dis += abs(x - customer[i][0]) + abs(y - customer[i][1])
                f(customer[i][0], customer[i][1])
                visited[i] = 0
                dis -= abs(x - customer[i][0]) + abs(y - customer[i][1])

for tc in range(1, int(input()) + 1):
    N = int(input())
    xyli = list(map(int, input().split()))
    customer = [[0, 0] for _ in range(N)]
    for i in range(4, len(xyli), 2):
        customer[i//2 - 2][0] = xyli[i]
        customer[i//2 - 2][1] = xyli[i + 1]
    visited = [0] * N
    dis, mindis = 0, 200 * (N + 2)
    f(xyli[0], xyli[1])
    print('#{} {}'.format(tc, mindis))