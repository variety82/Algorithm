
# coding: utf-8

# In[6]:


"""
2021-08-04

idea: 다익스트라 알고리즘을 활용하여 계산 후 제일 먼 거리 개수 출력
"""

import heapq
n,m,c=map(int,input().split())
INF=int(1e9)
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if(distance[now]<dist):
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if(cost<distance[i[0]]):
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(1)
cnt=0
max_d=0
for d in distance:
    if(d!=INF or d!=0):
        cnt+=1
        max_d=max(-1,d)
print(max_d,cnt)

