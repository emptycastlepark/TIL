def solution(n):
    if n <= 1:
        return n
    else:
        fibo = [0, 1]
        for i in range(2, n+1):
            fibo.append(fibo[-1] + fibo[-2])
        return fibo[-1] % 1234567

# # 재귀
# def solution2(n):
#     def fibo(n):
#         if n <= 1:
#             return n
#         else:
#             return fibo(n-1) + fibo(n-2)
#     return fibo(n) % 1234567