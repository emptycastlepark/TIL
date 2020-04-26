# 힙 정렬
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            answer = -1
            break
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
    return answer

# # remove, apppend (시간초과)
# def solution(scoville, K):
#     answer = 0
#     if min(scoville) >= K:
#         pass
#     else:
#         flag = 1
#         while len(scoville) > 1:
#             answer += 1
#             low1 = min(scoville)
#             scoville.remove(min(scoville))
#             low2 = min(scoville)
#             scoville.remove(min(scoville))
#             new = low1 + (low2 * 2)
#             scoville.append(new)
#             if min(scoville) >= K:
#                 flag = 0
#                 break
#         if flag:
#             answer = -1
#     return answer