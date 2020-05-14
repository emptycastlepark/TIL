def solution(operations):
    answer, newop, queue = [0, 0], [], []
    for i in operations:
        newop.append([i[0], int(i[2:])])
    for o, d in newop:
        if o == 'I':
            queue.append(d)
        else:
            if queue:
                if d == 1:
                    queue.remove(max(queue))
                else:
                    queue.remove(min(queue))
    if queue:
        answer = [max(queue), min(queue)]
    return answer