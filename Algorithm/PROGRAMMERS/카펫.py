def solution(brown, red):
    size = brown + red
    for i in range(3, size//3 + 1):
        if size % i == 0:
            if 2 * (size//i + i) - 4 == brown and (size//i - 2) * (i - 2) == red:
                break
    return [size//i, i]