def solution(num, cnt):
    global maxnum, minnum
    if cnt == N - 1:
        if num > maxnum:
            maxnum = num
        if num < minnum:
            minnum = num
    for i in range(4):
        if cal[i] > 0:
            cal[i] -= 1
            if i == 0:
                solution(num + numbers[cnt + 1], cnt + 1)
            elif i == 1:
                solution(num - numbers[cnt + 1], cnt + 1)
            elif i == 2:
                solution(num * numbers[cnt + 1], cnt + 1)
            else:
                if num < 0:
                    solution(-(abs(num) // numbers[cnt + 1]), cnt + 1)
                else:
                    solution(num // numbers[cnt + 1], cnt + 1)
            cal[i] += 1

N = int(input())
numbers = list(map(int, input().split()))
cal = list(map(int, input().split()))
maxnum, minnum = -10 ** 10, 10 ** 10
solution(numbers[0], 0)
print(maxnum)
print(minnum)