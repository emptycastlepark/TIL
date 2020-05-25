import heapq
def solution(stock, dates, supplies, k):
    answer, idx, h = 0, 0, []
    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] > stock:
                break
            heapq.heappush(h, -supplies[i])
            idx = i + 1
        stock += heapq.heappop(h) * (-1)
        answer += 1
    return answer