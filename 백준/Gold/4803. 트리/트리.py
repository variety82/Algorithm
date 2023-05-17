import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def find(parent, x):
    if (parent[x] != x):
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b


def check_tree_cnt(parent):
    cnt = 0
    candidate = set(parent[1:])
    if (0 in candidate):
        candidate.discard(0)
    for element in candidate:
        if (parent[element] != 0):
            cnt += 1
    return cnt


T = 1
while (True):
    N, M = map(int, input().split())
    if (N == 0 and M == 0):
        break

    parent = [int(x) for x in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        if (find(parent, a) != find(parent, b)):
            union(parent, a, b)
        else:
            parent[find(parent, a)] = 0

    for i in range(N + 1):
        find(parent, i)

    answer = check_tree_cnt(parent)

    if (answer == 0):
        print(f"Case {T}: No trees.")
    elif (answer == 1):
        print(f"Case {T}: There is one tree.")
    else:
        print(f"Case {T}: A forest of {answer} trees.")
    T += 1
