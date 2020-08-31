kd, sd, N = map(str, input().split())
kd = [8 - int(kd[1]), ord(kd[0]) - 65]
sd = [8 - int(sd[1]), ord(sd[0]) - 65]

for _ in range(int(N)):
    com = input()
    if com == 'R':
        if kd[1] + 1 < 8:
            if kd[0] != sd[0] or kd[1] + 1 != sd[1]:
                kd[1] += 1
            else:
                if sd[1] + 1 < 8:
                    kd[1] += 1
                    sd[1] += 1
    elif com == 'L':
        if kd[1] - 1 >= 0 :
            if kd[0] != sd[0] or kd[1] - 1 != sd[1]:
                kd[1] -= 1
            else:
                if sd[1] - 1 >= 0:
                    kd[1] -= 1
                    sd[1] -= 1
    elif com == 'B':
        if kd[0] + 1 < 8:
            if kd[0] + 1 != sd[0] or kd[1] != sd[1]:
                kd[0] += 1
            else:
                if sd[0] + 1 < 8:
                    kd[0] += 1
                    sd[0] += 1
    elif com == 'T':
        if kd[0] - 1 >= 0:
            if kd[0] - 1 != sd[0] or kd[1] != sd[1]:
                kd[0] -= 1
            else:
                if sd[0] - 1 >= 0:
                    kd[0] -= 1
                    sd[0] -= 1
    elif com  == 'RT':
        if kd[0] - 1 >= 0 and kd[1] + 1 < 8:
            if kd[0] - 1 != sd[0] or kd[1] + 1 != sd[1]:
                kd[0] -= 1
                kd[1] += 1
            else:
                if sd[0] - 1 >= 0 and sd[1] + 1 < 8:
                    kd[0] -= 1
                    kd[1] += 1
                    sd[0] -= 1
                    sd[1] += 1
    elif com  == 'LT':
        if kd[0] - 1 >= 0 and kd[1] - 1 >= 0:
            if kd[0] - 1 != sd[0] or kd[1] - 1 != sd[1]:
                kd[0] -= 1
                kd[1] -= 1
            else:
                if sd[0] - 1 >= 0 and sd[1] - 1 >= 0:
                    kd[0] -= 1
                    kd[1] -= 1
                    sd[0] -= 1
                    sd[1] -= 1
    elif com  == 'RB':
        if kd[0] + 1 < 8 and kd[1] + 1 < 8:
            if kd[0] + 1 != sd[0] or kd[1] + 1 != sd[1]:
                kd[0] += 1
                kd[1] += 1
            else:
                if sd[0] + 1 < 8 and sd[1] + 1 < 8:
                    kd[0] += 1
                    kd[1] += 1
                    sd[0] += 1
                    sd[1] += 1
    else:
        if kd[0] + 1 < 8 and kd[1] - 1 >= 0:
            if kd[0] + 1 != sd[0] or kd[1] - 1 != sd[1]:
                kd[0] += 1
                kd[1] -= 1
            else:
                if sd[0] + 1 < 8 and sd[1] - 1 >= 0:
                    kd[0] += 1
                    kd[1] -= 1
                    sd[0] += 1
                    sd[1] -= 1

print(str(chr(65 + kd[1])) + str(8 - kd[0]))
print(str(chr(65 + sd[1])) + str(8 - sd[0]))