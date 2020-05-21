for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))
    group = [[]*(N+1) for _ in range(N+1)]
    for i in range(0, len(paper) - 1, 2):
        group[paper[i]].append(paper[i+1])
        group[paper[i+1]].append(paper[i])
    cnt, checked = 0, [0] * (N + 1)
    for i in range(len(paper)):
        if checked[paper[i]] == 0:
            queue = [paper[i]]; checked[paper[i]] = 1
            while queue:
                q = queue.pop(0)
                for i in group[q]:
                    if checked[i] == 0:
                        checked[i] = 1
                        queue.append(i)
            cnt += 1
    cnt += checked.count(0) - 1
    print('#{} {}'.format(tc, cnt))