for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    friend = [[] * (N + 1) for _ in range(N + 1)]
    invite = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        friend[a].append(b)
        if a == 1:
            invite[b] = 1
        else:
            friend[b].append(a)
    for f in friend[1]:
        for f2 in friend[f]:
            invite[f2] = 1
    print('#{} {}'.format(tc, invite.count(1)))