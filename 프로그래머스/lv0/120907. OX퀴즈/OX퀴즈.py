def is_correct(expression):
    arr = expression.split(" ")
    pre = int(arr[0])
    oper = arr[1]
    post = int(arr[2])
    answer = int(arr[4])

    if(oper == "-"):
        if(pre - post == answer):
            return True
        return False
    else:
        if(pre + post == answer):
            return True
        return False

def solution(quiz):
    answer = []
    for expression in quiz:
        if(is_correct(expression)):
            answer.append("O")
        else:
            answer.append("X")
    return answer