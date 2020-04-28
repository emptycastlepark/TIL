def solution(N, number):
    answer, numli = -1, []
    for i in range(1, 9):
        numbers = set(); numbers.add(int(str(N) * i))
        for j in range(i - 1):
            for x1 in numli[j]:
                for x2 in numli[-1 - j]:
                    numbers.add(x1 + x2)
                    numbers.add(x1 - x2)
                    numbers.add(x1 * x2)
                    if x2 != 0:
                        numbers.add(x1 // x2)
        if number in numbers:
            answer = i
            break
        numli.append(numbers)
    return answer