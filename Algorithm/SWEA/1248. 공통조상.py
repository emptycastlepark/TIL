def f(tree):
    global cnt
    try:
        cnt += len(child[tree])
    except:
        pass
    for i in child[tree]:
        f(i)

for tc in range(1, int(input()) + 1):
    V, E, A, B = map(int, input().split())
    child = {i: [] for i in range(1, V + 1)}
    parent = {}
    node = list(map(int, input().split()))
    for i in range(0, len(node), 2):
        parent_node = node[i]
        child_node = node[i + 1]
        child[parent_node].append(child_node)
        parent[child_node] = parent_node
    temp, parent_A = A, []
    while True:
        try:
            parent_A.append(parent[temp])
        except:
            break
        temp = parent[temp]
    parent_B = parent[B]
    while parent_B not in parent_A:
        parent_B = parent[parent_B]
    cnt = 1
    f(parent_B)
    print('#{} {} {}'.format(tc, parent_B, cnt))