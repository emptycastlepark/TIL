for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    Nli = list(map(int, input().split()))
    Mli = list(map(int, input().split()))
    Nli.sort(); cnt = 0
    for m in Mli:
        l, r, flag = 0, N - 1, None
        mid = (l + r) // 2
        while l <= r:
            if m == Nli[mid]:
                cnt += 1
                break
            elif m < Nli[mid] and flag != 0:
                r, flag = mid - 1, 0
                mid = (l + r) // 2
            elif m > Nli[mid] and flag != 1:
                l, flag = mid + 1, 1
                mid = (l + r) // 2
            else:
                break
    print('#{} {}'.format(tc, cnt))