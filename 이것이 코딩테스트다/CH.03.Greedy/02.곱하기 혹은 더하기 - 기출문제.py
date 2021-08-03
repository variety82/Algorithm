
# coding: utf-8

# In[31]:


"""
2021-08-03

idea:연산하는 숫자 중 하나라도 1보다 작으면 더하는게 더 큰 값을 낳고 아니면 곱하는게 더 커진다. 
     차례대로 체크하면서 연산해나가면 된다 
"""
N=list(input())
for i in range(len(N)):
    N[i]=int(N[i])


for i in range(len(N)-1):
    if(N[i]<=1 or N[i+1]<=1):
        N[i+1]=N[i]+N[i+1]
    else:
        N[i+1]=N[i]*N[i+1]
        
print(N[-1])

