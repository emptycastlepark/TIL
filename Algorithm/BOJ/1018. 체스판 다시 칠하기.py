wb = 'WB'
c1, c2 = [[None] * 8 for _ in range(8)], [[None] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        c1[i][j], c2[i][j] = wb[(i + j) % 2], wb[(i + j + 1) % 2]

N, M = map(int, input().split())
board = [input() for _ in range(N)]
ans = 64
for i in range(N):
    if i + 7 == N:
        break
    for j in range(M):
        if j + 7 == M:
            break
        temp = board[i:i+8]
        cnt1, cnt2 = 0, 0
        for t in range(8):
            temp[t] = temp[t][j:j+8]
            for c in range(8):
                if temp[t][c] != c1[t][c]:
                    cnt1 += 1
                if temp[t][c] != c2[t][c]:
                    cnt2 += 1
        ans = min(ans, cnt1, cnt2)
print(ans)