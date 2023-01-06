def remove_food(food):
    for i in range(1, len(food)):
        if(food[i] % 2 == 1):
            food[i] -= 1
        food[i] //= 2            
    return food


def is_exist(item):
    return item == 0


def make_food_seq(food):
    seq = ""
    idx = 1
    while(idx != len(food)):
        if(is_exist(food[idx])):
            idx += 1
            continue
        seq += str(idx)
        food[idx] -= 1
    return seq


def solution(food):
    food = remove_food(food)
    seq = make_food_seq(food)
    answer = seq + "0" + seq[::-1]

    return answer