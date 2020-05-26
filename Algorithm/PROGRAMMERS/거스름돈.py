def solution(n, money):
    money.sort()
    dp = [0] * (n+1); dp[0] = 1
    for i in range(money[0], n+1, money[0]):
        dp[i] = 1
    for i in range(1, len(money)):
        for j in range(1, n+1):
            if j >= money[i]:
                dp[j] += dp[j-money[i]]
    return dp[-1] % 1000000007