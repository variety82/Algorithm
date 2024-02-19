def convert_decimal_to_bin(arr, n):
    arr = [list(map(int, (bin(x)[2:]))) for x in arr]
    for idx, row in enumerate(arr):
        if len(row) < n:
            for _ in range(n - len(row)):
                row.insert(0, 0)
                arr[idx] = row
    return arr

def solution(n, arr1, arr2):
    arr1 = convert_decimal_to_bin(arr1, n)
    arr2 = convert_decimal_to_bin(arr2, n)
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr1[i][j] or arr2[i][j]:
                arr[i][j] = "#"
            else:
                arr[i][j] = " "
        arr[i] = "".join(arr[i])
    return arr