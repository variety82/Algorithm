from itertools import combinations
def solution(number):
    arr = list(combinations(number, 3))
    answer = len([x for x in arr if sum(x) == 0])

    return answer