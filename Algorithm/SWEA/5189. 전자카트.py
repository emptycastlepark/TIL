def f(i):
    global answer, cnt
    if 0 not in checked:
        if cnt + arr[i][0] < answer:
            answer = cnt + arr[i][0]
    else:
        for j in range(len(arr[i])):
            if checked[j] != 1 and cnt + arr[i][j] < answer:
                checked[j] = 1
                cnt += arr[i][j]
                f(j)
                checked[j] = 0
                cnt -= arr[i][j]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        arr[i][i] = 101
    checked = [0]*N; checked[0] = 1
    answer, cnt= 100 * (N**2), 0
    f(0)
    print('#{} {}'.format(tc, answer))