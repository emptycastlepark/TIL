def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    checked = [0] * len(routes)
    while 0 in checked:
        camera = routes[checked.index(0)][1]
        checked[checked.index(0)] = 1
        answer += 1
        for i in range(1, len(routes)):
            if routes[i][0] <= camera <= routes[i][1] and checked[i] != 1:
                checked[i] = 1
    return answer