def solution(s):
    si, slist = 0, []
    for i in range(len(s)):
        if s[i] == ' ':
            slist.append(s[si:i])
            si = i+1
    slist.append(s[si:])
    answer = slist[0].capitalize()
    for i in range(1, len(slist)):
        answer += (' ' + slist[i].capitalize())
    return answer