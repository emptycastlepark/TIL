def solution(num, cnt):
    global maxnum, minnum
    if cnt == N - 1:
        if num > maxnum:
            maxnum = num
        if num < minnum:
            minnum = num
        return
    for i in range(N - 1):
        if checked[i] != 1:
            checked[i] = 1
            if cal2[i] == 0:
                solution(num + numbers[cnt + 1], cnt + 1)
            elif cal2[i] == 1:
                solution(num - numbers[cnt + 1], cnt + 1)
            elif cal2[i] == 2:
                solution(num * numbers[cnt + 1], cnt + 1)
            else:
                if num < 0:
                    solution(-(abs(num) // numbers[cnt + 1]), cnt + 1)
                else:
                    solution(num // numbers[cnt + 1], cnt + 1)
            checked[i] = 0

N = int(input())
numbers = list(map(int, input().split()))
cal = list(map(int, input().split()))
cal2 = []
for i in range(4):
    for _ in range(cal[i]):
        cal2.append(i)
checked = [0] * (N - 1)
maxnum, minnum = -10 ** 10, 10 ** 10
solution(numbers[0], 0)
print(maxnum)
print(minnum)