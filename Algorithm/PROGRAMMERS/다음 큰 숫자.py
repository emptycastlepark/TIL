def solution(n):
    cnt, b = 0, str(bin(n))
    for i in range(len(b)):
        if b[i] == '1':
            cnt += 1
    while True:
        n += 1
        cnt2, b = 0, str(bin(n))
        for i in range(len(b)):
            if b[i] == '1':
                cnt2 += 1
        if cnt2 == cnt:
            break
    return n