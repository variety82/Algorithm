import sys
sys.setrecursionlimit(int(1e5))

input = sys.stdin.readline

def find(parent, x):
    if (x != parent[x]):
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(a, b):
    a = find(parent, a)
    b = find(parent, b)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b


def play(airplane):
    global answer
    a = find(parent, airplane)
    if (a == 0):
        return -1
    if (a == airplane):
        union(airplane, airplane - 1)
        answer += 1
        return 0
    else:
        play(a)


G = int(input())
P = int(input())
airplanes = [int(input()) for _ in range(P)]
parent = [x for x in range(G + 1)]
answer = 0

for airplane in airplanes:
    if (play(airplane) == -1):
        break

print(answer)
