def solution(t, p):
    answer = 0
    p_length = len(p)
    for i in  range(len(t) - p_length + 1):
        if int(t[i:i+p_length]) <= int(p):
            answer += 1
    return answer