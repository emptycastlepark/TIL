case = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
checked = [[0] * 6 for _ in range(6)]
flag = 1
for i in range(36):
    com = input()
    ni, nj = ord(com[0]) - 65, 6 - int(com[1])
    # 처음 시작 좌표 저장
    if not i:
        si, sj = ni, nj
    # 이동가능 여부, 방문 여부 체크
    else:
        if (ni - bi, nj - bj) not in case or checked[ni][nj]:
            print('Invalid')
            flag = 0
            break
    checked[ni][nj] = 1
    bi, bj = ni, nj
# 36번 입력까지 제대로 이동했을 경우.
if flag:
    # 마지막 좌표에서 처음 좌표로 갈 수 있는지 체크
    if (si - bi, sj - bj) in case:
        print('Valid')
    else:
        print('Invalid')