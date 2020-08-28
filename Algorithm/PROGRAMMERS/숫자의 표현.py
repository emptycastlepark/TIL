def solution(n):
    answer = 0
    for start in range(1, n + 1):
        temp = 0
        for num in range(start, n + 1):
            temp += num
            if temp > n:
                break
            elif temp == n:
                answer += 1
                break

    return answer