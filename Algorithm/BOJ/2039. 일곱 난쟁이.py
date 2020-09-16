from itertools import combinations

dwarf = [None] * 9
for i in range(9):
    dwarf[i] = int(input())
dwarf_combi = list(combinations(dwarf, 7))
for d_c in dwarf_combi:
    if sum(d_c) == 100:
        d_c = sorted(list(d_c))
        for d in d_c:
            print(d)
        break