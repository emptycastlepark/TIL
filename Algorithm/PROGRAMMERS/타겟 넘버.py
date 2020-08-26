def solution(numbers, target):
    def dfs(num, idx):
        nonlocal answer
        if idx == len(numbers):
            if num == target:
                answer += 1
            return

        dfs(num + numbers[idx], idx + 1)
        dfs(num - numbers[idx], idx + 1)

    answer = 0
    dfs(0, 0)

    return answer