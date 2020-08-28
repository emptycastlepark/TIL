def solution(s):
    numli = list(map(int, s.split(' ')))
    return str(min(numli)) + ' ' + str(max(numli))