import heapq
def solution(n, works):
    answer = 0
    if sum(works) > n:
        works = [-work for work in works]
        heapq.heapify(works)
        for i in range(n):
            heapq.heappush(works, heapq.heappop(works) + 1)
        for i in range(len(works)):
            answer += (works[i] ** 2)
    return answer