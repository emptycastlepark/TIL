def f(cnt):
    global maxnum
    if cnt == n:
        if int(''.join(numlist)) > maxnum:
            maxnum = int(''.join(numlist))
    else:
        for i in range(len(numlist) - 1):
            for j in range(i + 1, len(numlist)):
                numlist[i], numlist[j] = numlist[j], numlist[i]
                temp = int(''.join(numlist))
                if temp not in tempnum[cnt]:
                    tempnum[cnt].append(temp)
                    f(cnt + 1)
                numlist[i], numlist[j] = numlist[j], numlist[i]

for tc in range(1, int(input()) + 1):
    num, n = input().split()
    numlist, n = list(num), int(n)
    tempnum = [[]for _ in range(n)]
    maxnum = 0; f(0)
    print('#{} {}'.format(tc, maxnum))