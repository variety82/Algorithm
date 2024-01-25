def solution(arr):
    idx = arr.index(min(arr))
    arr.pop(idx)
    if arr == []:
        return [-1]
    return arr