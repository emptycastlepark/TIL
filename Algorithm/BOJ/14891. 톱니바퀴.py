def rotate(num, way):
    if way == 1:
        a = gear[num].pop()
        gear[num].insert(0, a)
    else:
        a = gear[num].pop(0)
        gear[num].append(a)

gear = [list(map(int, input())) for _ in range(4)]
K = int(input())
for _ in range(K):
    num, way = map(int, input().split())
    num -= 1
    if num == 0:
        if gear[num][2] != gear[num + 1][-2]:
            if gear[num + 1][2] != gear[num + 2][-2]:
                if gear[num + 2][2] != gear[num + 3][-2]:
                    rotate(num + 3, -way)
                rotate(num + 2, way)
            rotate(num + 1, -way)
    elif num == 1:
        if gear[num - 1][2] != gear[num][-2]:
            rotate(num - 1, -way)
        if gear[num][2] != gear[num + 1][-2]:
            if gear[num + 1][2] != gear[num +2][-2]:
                rotate(num + 2, way)
            rotate(num + 1, -way)
    elif num == 2:
        if gear[num][2] != gear[num + 1][-2]:
            rotate(num + 1, -way)
        if gear[num - 1][2] != gear[num][-2]:
            if gear[num - 2][2] != gear[num - 1][-2]:
                rotate(num - 2, way)
            rotate(num - 1, -way)
    else:
        if gear[num - 1][2] != gear[num][-2]:
            if gear[num - 2][2] != gear[num - 1][-2]:
                if gear[num - 3][2] != gear[num - 2][-2]:
                    rotate(num - 3, -way)
                rotate(num - 2, way)
            rotate(num - 1, -way)
    rotate(num, way)

point = 0
for i in range(4):
    if gear[i][0]:
        point += 2 ** i
print(point)