def solution(numbers, target):
    answer = 0
    def dfs(nth, num):
        if(nth == len(numbers)):
            if(num == target):
                nonlocal answer
                answer += 1
            return
        else:
            dfs(nth + 1, num + numbers[nth])
            dfs(nth + 1, num - numbers[nth])
    
    dfs(0, 0)
    
    return answer