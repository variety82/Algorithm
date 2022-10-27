A, B = map(int, input().split())
answer = 1e9


def dfs(A, B, cnt):
    global answer
    if (A == B):
        answer = min(answer, cnt)
    if (A > B):
        return

    dfs(A * 2, B, cnt + 1)
    dfs(int(str(A) + "1"), B, cnt + 1)


dfs(A, B, 0)
if (answer + 1 == 1000000001.0):
    print(-1)
else:
    print(answer + 1)
