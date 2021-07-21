
# coding: utf-8

# In[32]:


"""
2021-07-21

idea: 주어진 문제의 조건에 따라 순서대로 구현
     방문한 자리를 체크할 visited, 90도 회전구현이 키포인트인듯
     
"""

N,M=map(int,input().split()) #N by M size game_map
x,y,d=map(int,input().split())  #현재 위치 및 바라보고있는 방향,  0:북쪽 , 1:동쪽, 2: 남쪽, 3:서쪽
game_map=list()
for _ in range(N):
    game_map.append(list(map(int,input().split())))
    
visited=[[0]*M for _ in range(N)]  #방문했는지 안했는지 체크할 리스트 
dx=[-1,0,1,0]
dy=[0,1,0,-1]
d_type=[0,1,2,3]

cnt=1
check=0 #안간 방향이나 바다 체크 
flag=False

while(flag==False):
    
    #90도 회전 0,1,2,3이 순서대로 북,동,남,서라 인덱스 하나 밀면 됨 
    for i in range(len(d_type)):
        if(d==d_type[i]):
            d=d_type[i-1]
    
    nx=x+dx[d]
    ny=y+dy[d]
    
    if(game_map[nx][ny]==0 and visited[nx][ny]==0):
        x,y=nx,ny
        cnt+=1
        visited[nx][ny]=-1
        check=0
        continue
        
    else:
        check+=1
    
    # 4방향 다 방문한 경우 뒤로 빽 할 수 있는지 체크후 안되면 끝
    if(check==4):
        nx=x-dx[d]
        ny=y-dy[d]
        if(game_map[nx][ny]==0):
            x,y=nx,ny
        else:
            flag=True
            
print(cnt)

"""
회고 : 37line 뒤로는 생각이 어려워 조금의 힌트를 받았다, 내가 생각한건 for문으로 상하좌우 모두 체크한 후 방문가능 하거나 방문불가하면
그 뒤 상황을 이어나가는 방법이였는데 이동할 때 마다 check를 하는 방법이 더 간단하고 조금이라도 실행시간이 단축되는 방법인 것 같다.
90도 회전하는 방법도 해설에서는 아예 따로 함수로 구현하였는데 아이디어 측면에서는 동일한 것 같으나 따로 함수로 구현하는게 코드 수정 및 활용성 측면에서 더 효율적일 것 같다

"""
        
            
            

