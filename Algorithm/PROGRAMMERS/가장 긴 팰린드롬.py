def solution(s):
    i, flag = 1, 0
    while i < len(s):
        for j in range(i):
            if s[j:len(s)-i+j+1] == s[j:len(s)-i+j+1][::-1]:
                flag = 1
                break
        if flag:
            break
        else:
            i += 1
    return len(s) - i + 1