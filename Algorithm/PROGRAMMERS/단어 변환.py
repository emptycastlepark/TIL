def solution(begin, target, words):
    def f(word):
        nonlocal cnt, answer
        if word == target:
            if cnt < answer:
                answer = cnt
        else:
            for i in range(len(words)):
                tempcnt = 0
                if wordlist[i][1] != 1:
                    for j in range(len(word)):
                        if word[j] == wordlist[i][0][j]:
                            tempcnt += 1
                    if tempcnt == len(word) - 1:
                        cnt += 1
                        wordlist[i][1] = 1
                        f(wordlist[i][0])
                        cnt -= 1
                        wordlist[i][1] = 0

    answer, cnt, stack = len(words), 0, []
    if target in words:
        if begin in words:
            words.remove(begin)
        wordlist = [[0, 0] for _ in range(len(words))]
        for i in range(len(words)):
            wordlist[i][0] = words[i]
        f(begin)
    else:
        answer = 0
    return answer