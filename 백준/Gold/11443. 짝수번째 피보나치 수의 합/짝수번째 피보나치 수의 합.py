import sys
input = sys.stdin.readline


fibo_matrix = [[1, 1], [1, 0]]


def multiple_matrix(matrix1, matrix2):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] = (res[i][j] + matrix1[i][k]
                             * matrix2[k][j]) % 1_000_000_007
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


n = int(input())
fibo = pow(fibo_matrix, n)
print(fibo[0][0] - 1 if (n % 2 == 0) else fibo[0][1] - 1)
