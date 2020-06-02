def solution(N, road, K):
    answer = 0
    town = [[0] * (N + 1) for _ in range(N + 1)]
    time = [K+1] * (N + 1); time[1] = 0
    for s, e, t in road:
        if town[s][e] == 0:
            town[s][e], town[e][s] = t, t
        else:
            if t < town[s][e]:
                town[s][e], town[e][s] = t, t
    queue = [1]
    while queue:
        q = queue.pop(0)
        for t in range(2, N+1):
            if town[q][t] != 0:
                if time[t] > time[q] + town[q][t] and time[q] + town[q][t] <= K:
                    time[t] = time[q] + town[q][t]
                    queue.append(t)
    for t in time:
        if t <= K: answer += 1
    return answer