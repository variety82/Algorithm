def solution(food):
    answer = ''
    food = [food[i] // 2 for i in range(len(food))]
    for idx, val in enumerate(food):
        answer = answer + str(idx) * val
    answer = answer + str(0) + answer[::-1]
    return answer