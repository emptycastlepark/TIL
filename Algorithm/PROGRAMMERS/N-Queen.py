def solution(n):
    def diag(i, j):
        for k in range(i):
            if i - k == abs(j - column[k]): return True
        return False
    def N_Queen(i):
        nonlocal cnt
        if i == n:
            cnt += 1
        for j in range(n):
            if line[j]: continue
            if diag(i, j): continue
            line[j] = 1
            column[i] = j
            N_Queen(i + 1)
            line[j] = 0
    cnt = 0
    line, column = [0] * n, [0] * n
    N_Queen(0)
    return cnt