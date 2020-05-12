def solution(jobs):
    n = len(jobs)
    jobs.sort()
    start, time = jobs.pop(0)
    answer, end = time, time + start
    while jobs:
        ni = 0
        for i in range(1, len(jobs)):
            if jobs[i][0] > end:
                break
            else:
                if jobs[i][1] < jobs[ni][1]:
                    ni = i
        next = jobs.pop(ni)
        if next[0] <= end:
            answer += next[1] + (end - next[0])
            end += next[1]
        else:
            answer += next[1]
            end = sum(next)
    return answer // n