def solution(budgets, M):
    answer = 0
    minb, maxb = 0, max(budgets)
    while maxb >= minb:
        mid = (minb + maxb) // 2
        temp = [None] * len(budgets)
        for i in range(len(budgets)):
            if budgets[i] > mid:
                temp[i] = mid
            else:
                temp[i] = budgets[i]
        if sum(temp) > M:
            maxb = mid - 1
        else:
            answer, minb = mid, mid + 1
    return answer