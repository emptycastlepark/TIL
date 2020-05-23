def solution(weight):
    weight.sort()
    answer = 1
    for w in weight:
        if w > answer:
            break
        answer += w
    return answer