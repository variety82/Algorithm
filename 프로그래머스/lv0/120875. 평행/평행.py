from itertools import combinations

def make_gradient(arr):
    x, y = arr[0][0], arr[0][1]
    x1, y1 = arr[1][0], arr[1][1]

    gradient = (y - y1) / (x - x1)

    return gradient

def solution(dots):
    answer = 0
    candidates = list(combinations(dots, 2))
    
    for candidate in candidates:
        m = make_gradient(candidate)
        n = make_gradient([x for x in dots if x not in candidate])
        if(m == n ):
            answer = 1
            break
            
    return answer