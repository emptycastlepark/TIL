def solution(nums):
    mon, N = set(nums), len(nums)/2
    if len(mon) > N:
        answer = N
    else:
        answer = len(mon)
    return answer