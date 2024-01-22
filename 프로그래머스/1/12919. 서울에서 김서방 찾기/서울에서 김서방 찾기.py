def solution(seoul):
    answer = ''
    for idx, people in enumerate(seoul):
        if people == "Kim":
            answer = '김서방은 ' + str(idx) + '에 있다'
    return answer