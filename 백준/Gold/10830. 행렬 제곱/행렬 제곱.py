import sys
input = sys.stdin.readline

N, B = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

def multiple(matrix1, matrix2):
    multiple_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                multiple_matrix[i][j] += (matrix1[i][k] * matrix2[k][j])
            multiple_matrix[i][j] %= 1000
    return multiple_matrix

def power(matrix, B):
    if(B == 1):
        return matrix
    else:
        x = power(matrix, B // 2)
        if(B % 2 == 0):
            return multiple(x, x)
        else:
            return multiple(multiple(x, x), matrix)
        
answer = power(matrix, B)
for i in range(N):
    print(*[x % 1000 for x in answer[i]])