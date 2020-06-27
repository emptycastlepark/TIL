N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for a in A:
    cnt += 1
    if a > B:
        a -= B
        p, r = divmod(a, C)
        cnt += p
        if r:
            cnt += 1
print(cnt)