def solution(skill, skill_trees):
    cnt = 0
    for i in range(len(skill_trees)):
        temp = []
        for j in range(len(skill)):
            try:
                skill_idx = skill_trees[i].index(skill[j])
            except ValueError:
                skill_idx = 26
            temp.append(skill_idx)
        temp2 = sorted(temp)
        if temp == temp2:
            cnt += 1
    return cnt