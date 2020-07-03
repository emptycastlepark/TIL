def clean(i, j, d, cnt):
    if cnt == 4:
        di, dj = i - direction[d][0], j - direction[d][1]
        if room[di][dj] == 1:
            return
        else:
            clean(di, dj, d, 0)
    else:
        room[i][j] = 2
        d = (d - 1) % 4
        di, dj = i + direction[d][0], j + direction[d][1]
        if room[di][dj] == 0:
            clean(di, dj, d, 0)
        else:
            clean(i, j, d, cnt + 1)
N, M = map(int, input().split())
r, c, d = map(int, input().split())
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
room = [None] * N
for i in range(N):
    room[i] = list(map(int, input().split()))
answer = 0
clean(r, c, d, 0)
for c in room:
    answer += c.count(2)
print(answer)