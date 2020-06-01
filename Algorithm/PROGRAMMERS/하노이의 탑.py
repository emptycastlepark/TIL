def solution(n):
    def hanoi(num, start, end):
        if num > 0:
            hanoi(num-1, start, 6 - start - end)
            answer.append([start, end])
            hanoi(num-1, 6 - start - end, end)
    answer = []
    hanoi(n, 1, 3)
    return answer