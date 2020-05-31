import math
def solution(n, k):
    answer, people = [None] * n, [None] * n
    for i in range(n):
        people[i] = i+1
    i = 1
    while i <= n:
        s = math.factorial(n - i)
        answer[i - 1] = people[(k - 1) // s]
        people.pop((k - 1) // s)
        if k > s:
            k %= s
        i += 1
    return answer