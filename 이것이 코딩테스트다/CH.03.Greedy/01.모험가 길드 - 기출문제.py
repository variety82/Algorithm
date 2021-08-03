
# coding: utf-8

# In[15]:


"""
2021-07-30
idea: 내림차순으로 정렬후 pop을 사용해 해당 숫자보다 -1의 갯수 만큼 뺀 후 리스트가 남아있으면 그룹을 +1해주고 아니면 종료한다
      
"""
N=int(input())
adv=list((map(int,input().split())))

adv.sort(reverse=True)
cnt=0
while len(adv)!=0:
    p=adv.pop(0)
    if(len(adv)>=(p-1)):
        for i in range(p-1):
            adv.pop(i)
        cnt+=1
    else:
        break
print(cnt)


"""
회고 : N이 십만개밖에 되지 않아서 그냥 정렬후 pop을 사용하는 작업을 반복했는데 N이 커지면 속도가 느려질 것 같다.
    
       
"""

