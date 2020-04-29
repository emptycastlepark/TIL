def solution(n, lost, reserve):
    equal = set()
    for i in range(len(lost)):
        if lost[i] in reserve:
            equal.add(lost[i])
    for x in equal:
        lost.remove(x); reserve.remove(x)
    for i in range(len(lost)):
        if lost[i] - 1 in reserve:
            reserve.remove(lost[i] - 1)
        elif lost[i] + 1 in reserve:
            reserve.remove(lost[i] + 1)
        else:
            n -= 1
    return n