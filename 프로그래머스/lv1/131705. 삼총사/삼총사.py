from itertools import combinations

def count_sum_zero(candidates):
    cnt = 0
    for candidate in candidates:
        if(sum(candidate) == 0):
            cnt += 1
    return cnt



def solution(number):
    candidates = list(combinations(number, 3))
    answer = count_sum_zero(candidates)
    return answer