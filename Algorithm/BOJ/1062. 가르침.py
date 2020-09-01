# combination
from itertools import combinations

base_character = set('antatica')
N, K = map(int, input().split())
words = [set(input()) - base_character for _ in range(N)]
left_chars = set()
for word in words:
    left_chars = left_chars | word

if K - 5 < 0:
    print(0)
elif K - 5 >= len(left_chars):
    print(N)
else:
    char_combi = list(combinations(left_chars, K - 5))
    ans = 0
    for c_c in char_combi:
        temp_ans = 0
        for word in words:
            for w in word:
                if w not in c_c:
                    break
            else:
                temp_ans += 1
        ans = max(ans, temp_ans)
        if ans == N:
            break
    print(ans)


# # dfs
# def dfs(idx, cnt):
#     global ans
#     if cnt == K - 5:
#         temp_ans = 0
#         for word in words:
#             flag = 1
#             for w in word:
#                 if not learned[ord(w) - ord('a')]:
#                     flag = 0
#                     break
#             if flag:
#                 temp_ans += 1
#         ans = max(ans, temp_ans)
#         return
#
#     for i in range(idx, 26):
#         if not learned[i]:
#             learned[i] = 1
#             dfs(i + 1, cnt + 1)
#             learned[i] = 0
#
# base_character = set('antatica')
# N, K = map(int, input().split())
# words = [set(input()) - base_character for _ in range(N)]
# left_chars = set()
# for word in words:
#     left_chars = left_chars | word
#
# if K - 5 < 0:
#     print(0)
# elif K - 5 >= len(left_chars):
#     print(N)
# else:
#     ans = 0
#     learned = [0] * 26
#     for b_c in base_character:
#         learned[ord(b_c) - ord('a')] = 1
#     dfs(0, 0)
#     print(ans)