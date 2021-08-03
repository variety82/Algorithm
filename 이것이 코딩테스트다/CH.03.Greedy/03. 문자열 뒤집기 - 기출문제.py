
# coding: utf-8

# In[62]:


"""
2021-08-03

회고 : 0이 포함된 영역과 1이 포함된 영역을 세준 다음 적은 영역의 수를 출력하려했으나 실패...
       해설의 아이디어는 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중 더 적은 횟수를 가지는 경우를 출력
"""
"""
하다가 실패한 코드

S=input()
S_zero=S.find("0")

cnt_zero=0
S_one=S.find("1")

cnt_one=0
for i in range(S_zero,len(S)-1):
    if(S[i]!=S[i+1] and S[i+1]!="0"):
        cnt_zero+=1
    else:
        continue
for i in range(S_one,len(S)-1):
    if(S[i]!=S[i+1] and (S[i+1]!="1")):
        cnt_one+=1
    else:
        continue
print(cnt_zero,cnt_one)
"""

#해설 코드 
data=input()
cnt0=0
cnt1=0

if data[0]=="0":
    cnt1+=1
else:
    cnt0+=1
for i in range(len(data)-1):
    if(data[i]!=data[i+1]):
        if(data[i+1]=="1"):
            cnt0+=1
        else:
            cnt1+=1
print(min(cnt0,cnt1))

    
    

