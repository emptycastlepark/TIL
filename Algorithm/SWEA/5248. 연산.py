from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    checked = [0] * 1000001; checked[N] = 1
    queue = deque([[N, 0]])
    while True:
        num, cnt = queue.popleft()
        if num == M:
            break
        for i in range(4):
            tempnum = 0
            if i == 0:
                tempnum = num + 1
            elif i == 1:
                tempnum = num - 1
            elif i == 2:
                tempnum = num * 2
            else:
                tempnum = num - 10
            if 0 < tempnum <= 1000000 and checked[tempnum] == 0:
                checked[tempnum] = cnt + 1
                queue.append((tempnum, cnt + 1))
    print('#{} {}'.format(tc, checked[M]))