R, C, M = map(int, input().split())
shark = dict()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1; c -= 1
    shark[r, c] = (s, d, z)
ans = 0
for c in range(C):
    for r in range(R):
        if (r, c) in shark:
            ans += shark[r, c][2]
            del shark[r, c]
            break
    if c == C-1:
        break
    move_shark = dict()
    for s in shark:
        r, c = s[0], s[1]
        s, d, z = shark[r, c]
        if d < 3:
            temp = s % ((R - 1) * 2)
            for _ in range(temp):
                if d == 1:
                    if r == 0:
                        d = 2
                        r += 1
                    else:
                        r -= 1
                else:
                    if r == R - 1:
                        d = 1
                        r -= 1
                    else:
                        r += 1
        else:
            temp = s % ((C - 1) * 2)
            for _ in range(temp):
                if d == 3:
                    if c == C - 1:
                        d = 4
                        c -= 1
                    else:
                        c += 1
                else:
                    if c == 0:
                        d = 3
                        c += 1
                    else:
                        c -= 1
        if (r, c) not in move_shark:
            move_shark[r, c] = (s, d, z)
        else:
            if move_shark[r, c][2] < z:
                move_shark[r, c] = (s, d, z)
    shark = move_shark

print(ans)