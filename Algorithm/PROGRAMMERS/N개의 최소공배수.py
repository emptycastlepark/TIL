def solution(arr):
    def gcd(x, y):
        if x % y == 0:
            return y
        else:
            return gcd(y, (x % y))

    answer = 1
    for n in arr:
        answer = (answer * n) // gcd(answer, n)

    return answer



# from math import gcd
#
# def solution(arr):
#     while True:
#         a, b = arr.pop(), arr.pop()
#         arr.append((a * b) // gcd(a, b))
#         if len(arr) == 1:
#             return arr[0]