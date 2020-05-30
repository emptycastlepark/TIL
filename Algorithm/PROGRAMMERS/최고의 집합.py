def solution(n, s):
    answer = [-1]
    if s >= n:
        answer = [s//n] * n
        idx = - 1
        for i in range(s % n):
            answer[idx] += 1
            idx -= 1
    return answer