import math
def solution(n, stations, w):
    answer, start = 0, 1
    for s in stations:
        if start < s - w:
            answer += math.ceil((s - w - start) / (2 * w + 1))
        start = s + w + 1
    end = start - 1
    if end < n:
        answer += math.ceil((n - end) / (2 * w + 1))
    return answer