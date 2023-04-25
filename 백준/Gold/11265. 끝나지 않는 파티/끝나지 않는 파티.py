import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

def floyd():
    for k in range(N):
        for a in range(N):
            for b in range(N):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


floyd()
for _ in range(M):
    a, b, c = map(int, input().split())
    print("Enjoy other party" if graph[a-1][b-1] <= c else "Stay here")