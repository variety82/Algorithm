T = int(input())

def rot_90(m):
    rot = [[str(row[i]) for row in m[::-1]] for i in range(len(m[0]))]
    join_rot = [''.join(x) for x in rot]
    return join_rot


for test_case in range(1, T + 1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    rot_mat = [[] for _ in range(n)]

    mat_90 = rot_90(mat)
    mat_180 = rot_90(mat_90)
    mat_270 = rot_90(mat_180)

    arr = list(zip(mat_90, mat_180, mat_270))

    answer = [[int(row[i]) for i in range(len(arr[0]))] for row in arr]
    print(f"#{test_case}")
    for row in answer:
        print(*row)