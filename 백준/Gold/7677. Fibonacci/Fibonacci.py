import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline


fibo_matrix = [[1, 1], [1, 0]]


def multiple_matrix(matrix1, matrix2):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] = (res[i][j] + matrix1[i][k]
                             * matrix2[k][j]) % 10_000
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
    n = int(input())
    if (n == 0):
        print(0)
        continue
    if (n == -1):
        break
    fibo = pow(fibo_matrix, n)
    print(fibo[0][1])
