
# coding: utf-8

# In[27]:


"""
2021-08-11
idea:주어진 조건 그대로 구현하면 됨, N사이즈가 커서 뭔가 다른 방법이 있을 줄 알았으나 아님 
"""
N=input()
cut_num=(len(N)//2)
f,b=0,0
for i in range(cut_num):
    f+=int(N[i])
for j in range(cut_num,len(N)):
    b+=int(N[j])
if(f==b):
    print("LUCKY")
else:
    print("READY")

