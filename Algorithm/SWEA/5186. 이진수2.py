for tc in range(1, int(input())+1):
    N10, N2 = float(input()), ''
    i, flag = 1, 1
    while len(N2) < 13:
        if N10 >= 2 ** (-i):
            N2 += '1'; N10 -= 2 ** (-i)
            if N10 == 0:
                flag = 0
                break
        else:
            N2 += '0'
        i += 1
    if flag:
        N2 = 'overflow'
    print('#{} {}'.format(tc, N2))