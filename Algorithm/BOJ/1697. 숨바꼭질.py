from collections import deque

N, K = map(int, input().split())
time = [0] * 100001
queue = deque()
queue.append(N)

while queue:
    now = queue.popleft()
    if now == K:
        print(time[now])
        break
    for next in (now - 1, now + 1, now * 2):
        if 0 <= next < 100001 and not time[next]:
            time[next] = time[now] + 1
            queue.append(next)