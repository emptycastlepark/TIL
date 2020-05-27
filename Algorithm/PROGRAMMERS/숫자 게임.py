def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    for a in A:
        for b in B:
            if b <= a:
                break
            else:
                B.remove(b)
                answer += 1
                break
    return answer