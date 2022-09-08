from itertools import combinations_with_replacement
import copy
def solution(n, info):
    score = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    max_win_score = -1
    diff = 0
    answer = [-1]
    
    def cal_score(lion_arr, info):
        lion_score, apeach_score = (0, 0)
        for l, a, s in zip(lion_arr, info, score):
            if(a == l == 0):
                continue
            elif(l <= a):
                apeach_score += s
            else:
                lion_score += s
        return lion_score, apeach_score
    
    for candidates in combinations_with_replacement(list(range(10, -1, -1)), n):
        lion_arr = [0] * 11
        lion_score, apeach_score = (0, 0)
        for candi in candidates:
            lion_arr[candi] += 1

        lion_score, apeach_score = cal_score(lion_arr, info)
        if(lion_score > apeach_score):
            diff = lion_score - apeach_score
            if(diff > max_win_score):
                max_win_score = diff
                answer = copy.deepcopy(lion_arr)
    return answer

