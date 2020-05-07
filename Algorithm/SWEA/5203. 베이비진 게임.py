for tc in range(1, int(input())+1):
    card = list(map(int, input().split()))
    p1, p2, winner, flag = [0]*10, [0]*10, 0, 0
    for i in range(len(card)):
        if i % 2 == 0:
            p1[card[i]] += 1
        else:
            p2[card[i]] += 1
        if i >= 4:
            for j in range(10):
                if p1[j] == 3:
                    winner, flag = 1, 1
                    break
                if p2[j] == 3:
                    winner, flag = 2, 1
                    break
                if 0 < j < 9:
                    if 0 not in p1[j-1:j+2]:
                        winner, flag = 1, 1
                        break
                    if 0 not in p2[j-1:j+2]:
                        winner, flag = 2, 1
                        break
            if flag:
                break
    print('#{} {}'.format(tc, winner))