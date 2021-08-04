
# coding: utf-8

# In[11]:


"""
2021-08-04

idea: cost 1로 양방향으로 이동이 가능하게 그래프를 설정하고 플로이드 워셜 알고리즘을 이용해 해결
"""

N,M=map(int,input().split())
INF=int(1e9)
graph=[[INF]*(N+1) for _ in range(N+1)]
for a in range(1,N+1):
    for b in range(1,N+1):
        if(a==b):
            graph[a][b]=0
for _ in range(M):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
X,K=map(int,input().split())

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

if(graph[1][K]+graph[K][X]>=INF):
    print(-1)
else:
    print(graph[1][K]+graph[K][X])

