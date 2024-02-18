from itertools import combinations
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    nums_combi = list(combinations(nums, 3))
    for nums in nums_combi:
        if is_prime(sum(nums)):
            answer += 1
    return answer