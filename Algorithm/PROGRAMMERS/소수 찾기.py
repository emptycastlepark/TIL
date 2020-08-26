from itertools import permutations

def solution(numbers):
    ans = 0
    nums = set()
    for r in range(len(numbers)):
        temp = set(permutations(list(numbers), r + 1))
        for te in temp:
            nums.add(int("".join(te)))
    for n in nums:
        if n > 1:
            flag = 1
            for d_n in range(2, n//2 + 1):
                if n % d_n == 0:
                    flag = 0
                    break
            if flag:
                ans += 1

    return ans



# # 에라토스테네스의 체
#
# from itertools import permutations
#
# def solution(numbers):
#     nums = set()
#     for r in range(len(numbers)):
#         nums |= set(map(int, map("".join, permutations(list(numbers), r + 1))))
#     nums -= set(range(0, 2))
#     for i in range(2, int(max(nums) ** 0.5) + 1):
#         nums -= set(range(i * 2, max(nums) + 1, i))
#
#     return len(nums)