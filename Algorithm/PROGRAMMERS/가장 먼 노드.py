def solution(n, edge):
    answer = [0] * (n+1)
    node = [[]*(n+1)for _ in range(n+1)]
    for i, j in edge:
        node[i].append(j)
        node[j].append(i)
    visited = [0] * (n+1)
    queue, visited[1] = [1], 1
    while queue:
        q = queue.pop(0)
        for i in node[q]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                answer[i] = answer[q] + 1
    return answer.count(max(answer))