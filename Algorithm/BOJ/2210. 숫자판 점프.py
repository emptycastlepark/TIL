di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(i, j, num):
    if len(num) == 6:
        number.add(int(num))
        return

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < 5 and 0 <= nj < 5:
            dfs(ni, nj, num + board[ni][nj])

board = [list(input().split()) for _ in range(5)]
number = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])
print(len(number))