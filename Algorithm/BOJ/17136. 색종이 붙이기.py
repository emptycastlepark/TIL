def f(r, c, cnt):
    global ans
    if r >= 10:
        ans = min(ans, cnt)
        return
    if c >= 10:
        f(r + 1, 0, cnt)
        return
    if board[r][c]:
        for k in range(4, -1, -1):
            if paper[k] == 5:
                continue
            if r + k >= 10 or c + k >= 10:
                continue
            flag = 0
            for i in range(r, r + k + 1):
                for j in range(c, c + k + 1):
                    if board[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break
            if not flag and cnt + 1 < ans:
                for i in range(r, r + k + 1):
                    for j in range(c, c + k + 1):
                        board[i][j] = 0
                paper[k] += 1
                f(r, c + k + 1, cnt + 1)
                paper[k] -= 1
                for i in range(r, r + k + 1):
                    for j in range(c, c + k + 1):
                        board[i][j] = 1
    else:
        f(r, c + 1, cnt)

paper = [0] * 5
board = [list(map(int, input().split())) for _ in range(10)]
ans = 26
f(0, 0, 0)
if ans == 26:
    ans = -1
print(ans)