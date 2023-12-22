def solution(s):
    answer = 0
    while True:
        if s == "":
            return answer
        x = s[0]
        x_cnt = 0
        else_cnt = 0
        for idx, spelling in enumerate(s):
            if spelling == x:
                x_cnt += 1
            else:
                else_cnt += 1
            
            if x_cnt == else_cnt:
                s = s[idx+1:]
                answer += 1
                break
        else:
            answer += 1
            return answer