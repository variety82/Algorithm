def solution(arr1, arr2):
    answer = [[col1 + col2 for col1, col2 in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]            
    return answer