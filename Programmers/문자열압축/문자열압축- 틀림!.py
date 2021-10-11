
# coding: utf-8

# In[80]:


"""
2021-08-12
idea: 문자열을 앞에서부터 for문으로 size 1~문자열의길이 절반까지 쪼갠다. 앞뒤로 문자열을 비교해나가면서 같으면 압축,다르면압축하지 않는데
     비교해나갈 때 연속으로 다르거나 맨마지막 문자 판정을 유의해야한다.
     
"""
def solution(s):
    max_len=len(s)//2
    answer=1001
    for i in range(1,max_len+1):
            cnt=0
            #flag는 맨 마지막 문자의 판정을 위해 사용
            flag=False
            a=[s[j:j+i] for j in range(0,len(s),i)]
            if(len(a)==1):
                cnt=len(a[0])
                answer=min(answer,cnt)
                continue
            for k in range(len(a)-1):
                if(a[k]==a[k+1]):
                    flag=True
                    continue
                else:
                    # 연속해서 다르면 그 문자열 길이만큼만 더한다. 
                    if(a[k-1]!=a[k]):
                        cnt=cnt+len(a[k])
                    else:
                        cnt=cnt+(len(a[k])+1)
                    flag=False
            if(flag==True):
                cnt=cnt+len(a[k+1])+1
            else:
                cnt=cnt+len(a[k+1])
            answer=min(answer,cnt)
        
    return answer

"""
회고: 프로그래머스에서 돌리면 68/100이 나온다, 눈에보이는 테스트케이스에만 맞춰서 구현해서 그런듯... 전체를 생각하기  
"""

