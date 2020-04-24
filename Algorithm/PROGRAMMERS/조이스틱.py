def solution(name):
    name = list(name)
    aaa = ['A'] * len(name)
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = 0
    idx, right, left = 0, 1, 1
    while True:
        if name[idx] != 'A':
            if abc.index(name[idx]) > 13:
                answer += (26 - abc.index(name[idx]))
            else:
                answer += abc.index(name[idx])
            name[idx] = 'A'
        if name == aaa:
            break
        else:
            flag = 0
            for i in range(1, len(name)):
                if name[idx+i] != 'A':
                    break
                if name[idx-i] != 'A':
                    flag = 1
                    break
            answer += i
            if flag:
                idx -= i
            else:
                idx += i
    return answer