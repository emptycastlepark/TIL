def solution(n):
    if n <= 2:
        return n
    else:
        case = [1, 2]
        for i in range(2, n):
            case.append((case[-1] + case[-2]) % 1000000007)
        return case[-1]