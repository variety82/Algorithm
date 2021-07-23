
# coding: utf-8

# In[38]:


"""
2021-07-23

idea: 데이터 크기와 사이즈를 고려해 이진탐색으로 탐색 
"""
N=int(input())
goods_N=sorted(list(map(int,input().split())))
M=int(input())
goods_M=list(map(int,input().split()))

def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if(array[mid]==target):
        return True
    elif(array[mid]>target):
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
        
for i in range(len(goods_M)):
    if(binary_search(goods_N,goods_M[i],0,N-1)==True):
        print("Yes",end=' ')
    else:
        print("No",end=' ')
        
"""
회고 : 나머지는 다 해놓고 정작 인풋어레이를 정렬하지 않아 제대로 돌아가지않았다, 이진탐색의 탐색 조건 잘 확인! 
       해설을 보니 계수정렬 및 집합 자료형으로도 풀이가 가능했다. 문제 조건에는 써있지 않았는데 중복된 부품이 있다는 가정이 들어간 것 같다.
       
"""

