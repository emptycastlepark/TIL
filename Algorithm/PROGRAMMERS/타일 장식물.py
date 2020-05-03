def solution(N):
    def wh(n):
        if n == 1:
            return 4
        else:
            whlist = [4]
            for i in range(1, n):
                whlist.append(whlist[-1] + 2 * length[i])
            return whlist[-1]
    length = [1, 1]
    for i in range(2, N):
        length.append(length[-1] + length[-2])
    return wh(N)