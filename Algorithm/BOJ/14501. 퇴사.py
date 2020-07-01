N = int(input())
schedule = [None] * N
for i in range(N):
    schedule[i] = list(map(int, input().split()))
money = [schedule[i][1] for i in range(N)]
for date in range(N):
    if date + schedule[date][0] <= N:
        for prev in range(date):
            if schedule[prev][0] + prev <= date:
                money[date] = max(money[prev] + schedule[date][1], money[date])
    else:
        money[date] = 0
print(max(money))