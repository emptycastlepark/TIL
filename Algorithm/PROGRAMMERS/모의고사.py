def solution(answers):
    answer = []
    mathgiveup1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    mathgiveup2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    mathgiveup3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    i, idx1, idx2, idx3 = 0, 0, 0, 0
    while i < len(answers):
        if idx1 == len(mathgiveup1):
            idx1 -= len(mathgiveup1)
        if mathgiveup1[idx1] == answers[i]:
            cnt1 += 1
        if idx2 == len(mathgiveup2):
            idx2 -= len(mathgiveup2)
        if mathgiveup2[idx2] == answers[i]:
            cnt2 += 1
        if idx3 == len(mathgiveup3):
            idx3 -= len(mathgiveup3)
        if mathgiveup3[idx3] == answers[i]:
            cnt3 += 1
        i += 1; idx1 += 1; idx2 += 1; idx3 += 1
    temp = [[cnt1, 1], [cnt2, 2], [cnt3, 3]]
    temp.sort()
    answer.append(temp[-1][1])
    if temp[-1][0] == temp[-2][0]:
        answer.append(temp[-2][1])
        if temp[-2][0] == temp[-3][0]:
            answer.append(temp[-3][1])
    return sorted(answer)