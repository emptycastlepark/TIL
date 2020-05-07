for tc in range(1, int(input())+1):
    N = int(input())
    Nlist = [list(map(int, input().split()))for _ in range(N)]
    Nlist.sort(key=lambda x: x[1])
    cnt, end = 0, 0
    for i in range(N):
        if end <= Nlist[i][0]:
            cnt += 1; end = Nlist[i][1]
    print('#{} {}'.format(tc, cnt))