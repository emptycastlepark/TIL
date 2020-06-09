def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    char1, char2 = [], []
    inter = 0
    for i in range(len(str1) - 1):
        temp = str1[i:i + 2]
        if temp.isalpha():
            char1.append(temp)
    for i in range(len(str2) - 1):
        temp = str2[i:i + 2]
        if temp.isalpha():
            char2.append(temp)
            if temp in char1:
                char1.remove(temp)
                inter += 1
    union= len(char1) + len(char2)
    if union == 0:
        return 65536
    else:
        return int((inter / union) * 65536)