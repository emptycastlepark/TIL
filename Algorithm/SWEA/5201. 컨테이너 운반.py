for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split())); W.sort(reverse=True)
    T = list(map(int, input().split())); T.sort(reverse=True)
    answer = 0
    while True:
        if T[0] >= W[0]:
            answer += W[0]
            W.pop(0); T.pop(0)
        else:
            W.pop(0)
        if len(W) == 0 or len(T) == 0:
            break
    print('#{} {}'.format(tc, answer))