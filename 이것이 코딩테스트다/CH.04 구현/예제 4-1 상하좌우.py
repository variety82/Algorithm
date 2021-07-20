
# coding: utf-8

# In[21]:


"""
2021-07-15

idea:단순 구현문제, 주어진 입력에 따라 상하좌우로 이동하면서 좌표를 수정해나간다

회고 ? : 
사각형을 벗어나면 좌표수정을 하지말고 벗어나야하는데 처음엔 for문의 안에다 넣었을 때 벗어남에도 갱신이 되었다
command와 move_type이 맞는경우는 한가지 밖에 없어서 continue해도 의미가 없기때문
그래서 수행이 끝난 for문과 동일한 라인에 맞춰야된다. 
"""


N=int(input())
move=list(input().split())
dx=[0,0,-1,1]  # 상,하
dy=[-1,1,0,0]  # 좌,우
x,y=1,1
move_type=["L","R","U","D"]

for command in move:
    for i in range(len(move_type)):
        if(command==move_type[i]):
            nx=x+dx[i]
            ny=y+dy[i]
    if(nx<1 or ny<1 or nx>N or ny>N):
        continue
    x,y=nx,ny
    
print(nx,ny)

