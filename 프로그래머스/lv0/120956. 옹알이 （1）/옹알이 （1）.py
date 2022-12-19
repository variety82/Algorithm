from itertools import permutations


def make_word(candidates, arr):
    for i in range(len(arr)):
        candidates.append("".join(arr[i]))

def solution(babbling):
    babblings = ["aya", "ye", "woo", "ma"]
    candidates = []
    
    
    for i in range(1, 5):
        make_word(candidates, list(permutations(babblings, i)))
    
    
    answer = len([word for word in babbling if word in candidates])
    return answer