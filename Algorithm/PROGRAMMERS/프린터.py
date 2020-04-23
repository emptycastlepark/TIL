def solution(priorities, location):
    myprint = [0]*len(priorities); myprint[location] = 1
    finish = []
    while True:
        out = priorities.pop(0)
        myout = myprint.pop(0)
        for i in range(len(priorities)):
            if priorities[i] > out:
                priorities.append(out)
                myprint.append(myout)
                break
        else:
            finish.append(out)
            if myout == 1:
                break
    return len(finish)