def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    delete = [[0] * n for _ in range(m)]
    while True:
        flag = 1
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != '0' and board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    delete[i][j], delete[i][j + 1], delete[i + 1][j], delete[i + 1][j + 1] = 1, 1, 1, 1
                    flag = 0
        if flag:
            break
        else:
            for i in range(m):
                for j in range(n):
                    if delete[i][j] == 1:
                        board[i][j], delete[i][j] = '1', 0
                        answer += 1
        for j in range(n):
            temp = ''
            for i in range(m - 1, -1, -1):
                temp += board[i][j]
            temp = temp.replace('1', '')
            for i in range(m):
                if i < len(temp):
                    board[m - 1 - i][j] = temp[i]
                else:
                    board[m - 1 - i][j] = '0'
    return answer