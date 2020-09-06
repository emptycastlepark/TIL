N, r, c = map(int, input().split())
ans = 0
while N > 0:
    temp = 2 ** (N - 1)
    # 2사분면
    if r < temp and c >= temp:
        ans += temp ** 2
        c -= temp
    # 3사분면
    elif r >= temp and c < temp:
        ans += 2 * (temp ** 2)
        r -= temp
    # 4사분면
    elif r >= temp and c >= temp:
        ans += 3 * (temp ** 2)
        r -= temp; c -= temp
    N -= 1
print(ans)