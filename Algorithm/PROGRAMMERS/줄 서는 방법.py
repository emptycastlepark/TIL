import math
def solution(n, k):
    answer = [None] * n
    people = list(range(1, n+1))
    i = 1
    while i <= n:
        s = math.factorial(n - i)
        answer[i - 1] = people[(k - 1) // s]
        people.pop((k - 1) // s)
        if k > s:
            k %= s
        i += 1
    return answer