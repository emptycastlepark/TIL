def solution(people, limit):
    people.sort(reverse=True)
    i, j, cnt = 0, len(people)-1, 0
    while i < j+1:
        if people[i] < limit:
            rest = limit - people[i]
            if people[j] <= rest:
                j -= 1
        i += 1; cnt += 1
    return cnt