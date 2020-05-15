def quick_sort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quick_sort(arr, l, p-1)
        quick_sort(arr, p+1, r)

def partition(arr, l, r):
    pivot = l
    while l < r:
        while l <= r and arr[l] <= arr[pivot]:
            l += 1
        while l <= r and arr[r] >= arr[pivot]:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
    arr[pivot], arr[r] = arr[r], arr[pivot]
    return r

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N - 1)
    print('#{} {}'.format(tc, arr[N//2]))