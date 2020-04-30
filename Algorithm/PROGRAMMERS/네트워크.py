def solution(n, computers):
    def f(j):
        for k in range(len(computers[j])):
            if computers[j][k] == 1 and checked[k] != 1:
                checked[k] = 1
                f(k)
    answer, checked = 0, [0] * n
    for i in range(len(computers)):
        if checked[i] != 1:
            checked[i] = 1
            f(i)
            answer += 1
    return answer