import sys
input = sys.stdin.readline


def multiple_matrix(matrix1, matrix2):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] = (res[i][j] + matrix1[i][k]
                             * matrix2[k][j]) % (mod)
    return res


def pow(a, n):
    if (n == 1):
        return a
    else:
        x = pow(a, n // 2)
        if (n % 2 == 0):
            return multiple_matrix(x, x)
        else:
            return multiple_matrix(multiple_matrix(x, x), a)


while (True):
    N, mod, P = map(int, input().split())
    if (N == 0 and mod == 0 and P == 0):
        break
    mat = [list(map(int, input().split())) for _ in range(N)]
    answer = pow(mat, P)
    for i in range(N):
        print(*answer[i])
    print()