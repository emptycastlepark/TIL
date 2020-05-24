def solution(n):
    if n <= 2:
        return n
    else:
        temp = [1, 2]
        for i in range(3, n+1):
            temp.append(temp[-1] + temp[-2])
        return temp[-1] % 1234567