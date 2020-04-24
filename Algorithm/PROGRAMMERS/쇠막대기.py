def solution(arrangement):
    cnt, bar = 0, []
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            bar.append('(')
        else:
            bar.pop()
            if arrangement[i-1] == '(':
                cnt += len(bar)
            else:
                cnt += 1
    return cnt