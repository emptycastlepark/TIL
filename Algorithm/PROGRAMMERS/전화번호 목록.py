def solution(phone_book):
    answer, flag = True, 0
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if j != i and phone_book[j][:len(phone_book[i])] == phone_book[i]:
                flag = 1
                break
        if flag:
            answer = False
            break
    return answer