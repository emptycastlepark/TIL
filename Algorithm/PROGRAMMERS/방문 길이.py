def solution(dirs):
    answer = []
    x = y = 0
    for d in dirs:
        if d == 'U':
            if y + 1 <= 5:
                y += 1
                if ((x, y - 1), (x, y)) not in answer:
                    answer.append(((x, y - 1), (x, y)))
                    answer.append(((x, y), (x, y - 1)))
        elif d == 'D':
            if y - 1 >= -5:
                y -= 1
                if ((x, y + 1), (x, y)) not in answer:
                    answer.append(((x, y + 1), (x, y)))
                    answer.append(((x,y), (x, y + 1)))
        elif d == 'R':
            if x + 1 <= 5:
                x += 1
                if ((x - 1, y), (x, y)) not in answer:
                    answer.append(((x - 1, y), (x, y)))
                    answer.append(((x, y), (x - 1, y)))
        else:
            if x - 1 >= -5:
                x -= 1
                if ((x + 1, y), (x, y)) not in answer:
                    answer.append(((x + 1, y), (x, y)))
                    answer.append(((x, y), (x + 1, y)))
    return len(answer) // 2