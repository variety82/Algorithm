
# coding: utf-8

# In[ ]:


def solution(answers):
    
    ansLen = len(answers)

    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    q1, r1 = divmod(ansLen, len(num1))
    q2, r2 = divmod(ansLen, len(num2))
    q3, r3 = divmod(ansLen, len(num3))
    
    num1 = num1 * q1 + num1[:r1]
    num2 = num2 * q2 + num2[:r2]
    num3 = num3 * q3 + num3[:r3]
    
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(ansLen):
        if(answers[i] == num1[i]):
            cnt1 += 1
        if(answers[i] == num2[i]):
            cnt2 += 1
        if(answers[i] == num3[i]):
            cnt3 += 1
        
    temp = [cnt1, cnt2, cnt3]
    answer = []
    
    for idx, value in enumerate(temp):
        if(max(temp) == value):
            answer.append(idx+1)
    return answer

