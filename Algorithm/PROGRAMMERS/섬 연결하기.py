def solution(n, costs):
    answer = 0
    checked = [0] * n; checked[0] = 1
    costs.sort(key=lambda x: x[2])
    while 0 in checked:
        for i, j, c in costs:
            if checked[i] == 1 or checked[j] == 1:
                if checked[i] == 1 and checked[j] == 1:
                    pass
                else:
                    checked[i], checked[j] = 1, 1
                    answer += c
                    break
    return answer