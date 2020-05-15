def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
        return merge(left, right)

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    result = [0] * (len(left) + len(right))
    i = l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[i] += left[l]
            i += 1; l += 1
        else:
            result[i] += right[r]
            i += 1; r += 1
    while l < len(left):
        result[i] += left[l]
        i += 1; l += 1
    while r < len(right):
        result[i] += right[r]
        i += 1; r += 1
    return result

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print('#{} {} {}'.format(tc, merge_sort(arr)[N//2], cnt))