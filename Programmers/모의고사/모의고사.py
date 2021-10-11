
# coding: utf-8

# In[ ]:


'''
2021-10-11
idea : 학생 1,2,3 의 문제개수를 위해 divmod를 사용하여 몫, 나머지를 구하고 답안지 사이즈에 맞춰서 늘려줬다
그 후 완전탐색을 이용해 학생과 답안지를 비교해 정답개수를 카운트 해주고 오름차순으로 answer에 추가한다. 
'''

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

'''
회고 : 처음엔 맥스값을 찾고 정렬하기 위해 정렬을 한 후 사용했는데 그건 정답개수였고, 그 후 학생 번호와 정답개수를 매칭시키는데 조금 애먹었다
enumerate를 사용해서 value에 따라 idx에 1을 더해 추가하면 됐따!
'''

