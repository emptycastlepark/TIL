dir = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),
       'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)}

kd, sd, N = map(str, input().split())
kd = [8 - int(kd[1]), ord(kd[0]) - 65]
sd = [8 - int(sd[1]), ord(sd[0]) - 65]

for _ in range(int(N)):
    com = input()
    nkr, nkc = kd[0] + dir[com][0], kd[1] + dir[com][1]
    nsr, nsc = sd[0] + dir[com][0], sd[1] + dir[com][1]
    if 0 <= nkr < 8 and 0 <= nkc < 8:
        if nkr != sd[0] or nkc != sd[1]:
            kd[0], kd[1] = nkr, nkc
        else:
            if 0 <= nsr < 8 and 0 <= nsc < 8:
                kd[0], kd[1] = nkr, nkc
                sd[0], sd[1] = nsr, nsc

print(str(chr(65 + kd[1])) + str(8 - kd[0]))
print(str(chr(65 + sd[1])) + str(8 - sd[0]))