def count_seven(item):
    return str(item).count('7')

def solution(array):
    answer = 0
    for item in array:
        answer += count_seven(item)
    
    return answer