
# coding: utf-8

# In[59]:


"""
2021-08-11
idea:문자열을 앞에서 하나씩 체크하면서 영문자면 리스트에 추가,정수면 더하기 후에 최종적으로는 영문자는 오름차순정렬 후 합치기
"""
S=input()
str_list=[]
total=0
for i in range(len(S)):
    if(48<=ord(S[i])<=57):
        total+=int(S[i])
    else:
        str_list.append(S[i])
str_list.sort()
str_list=''.join(str_list)
print(f"{str_list}{total}")

"""
회고 : .isalpha()라는 함수가 있었다, 몰랐으니 ord를 이용해 체크한 것도 나쁘지 않은듯? 
"""


# In[60]:




