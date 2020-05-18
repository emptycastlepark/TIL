# 리스트
def solution(genres, plays):
    answer, album, i = [], [], 0
    for g, p in zip(genres, plays):
        album.append([p, i, g])
        i += 1
    album.sort(key=lambda x: (-x[0], x[1]))
    count = []
    for j in range(len(album)):
        for k in range(len(count)):
            if album[j][2] == count[k][1]:
                count[k][0] += album[j][0]
                break
        else:
            count.append([album[j][0], album[j][2]])
    count.sort(reverse=True)
    while count:
        genre = count.pop(0)[1]
        cnt = 0
        for j in range(len(album)):
            if album[j][2] == genre:
                answer.append(album[j][1])
                cnt += 1
            if cnt > 1:
                break
    return answer

# 딕셔너리
def solution2(genres, plays):
    answer = []
    countdict, musicdict = {}, {}
    for i in range(len(genres)):
        countdict[genres[i]] = countdict.get(genres[i], 0) + plays[i]
        musicdict[genres[i]] = musicdict.get(genres[i], []) + [(plays[i], i)]
    sortcount = sorted(countdict.items(), key=lambda x: -x[1])
    for genre, count in sortcount:
        musicdict[genre] = sorted(musicdict[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for play, idx in musicdict[genre][:2]]
    return answer