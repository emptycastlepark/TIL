from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    checked = [0] * 1000001; checked[N] = 1
    queue = deque([[N, 0]])
    while True:
        num, cnt = queue.popleft()
        if num == M:
            break
        tempnum = [num + 1, num - 1, num * 2, num - 10]
        for tn in tempnum:
            if 0 < tn <= 1000000 and checked[tn] == 0:
                checked[tn] = cnt + 1
                queue.append((tn, cnt + 1))
    print('#{} {}'.format(tc, checked[M]))