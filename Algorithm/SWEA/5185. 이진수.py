# bin, hex
for tc in range(1, int(input())+1):
    N, N16 = map(str, input().split())
    N10 = int(N16, 16)
    N2 = bin(N10)[2:]
    while len(N2) < 4 * int(N):
        N2 = '0' + N2
    print('#{} {}'.format(tc, N2))

# 비트연산
