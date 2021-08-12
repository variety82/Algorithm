
# coding: utf-8

# In[80]:


def solution(s):
    max_len=len(s)//2
    answer=1001
    for i in range(1,max_len+1):
            cnt=0
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

