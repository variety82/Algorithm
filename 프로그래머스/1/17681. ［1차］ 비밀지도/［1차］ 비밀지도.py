def convert_decimal_to_bin(arr1, arr2, n):
    arr = [list(map(int, (bin(x|y)[2:]))) for x, y in zip(arr1, arr2)]
    for idx, row in enumerate(arr):
        if len(row) < n:
            for _ in range(n - len(row)):
                row.insert(0, 0)
                arr[idx] = row
    return arr

def solution(n, arr1, arr2):
    arr = convert_decimal_to_bin(arr1, arr2, n)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                arr[i][j] = "#"
            else:
                arr[i][j] = " "
        arr[i] = "".join(arr[i])
    return arr