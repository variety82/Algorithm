# 최단 경로

___

## 가장 빠른 길 찾기

### Dijkstra 최단 경로 알고리즘

*특정한 노드에서 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘(음의 Edge가 없을 때 정상 동작)

1. 출발 노드를 기준으로 최단 거리 테이블을 초기화
1. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
1. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
1. 위 과정에서 '3','4'번을 반복. 

매번 가장 코스트가 적은 노드를 선택해 과정을 반복하기에 Greedy 알고리즘으로 분류된다.

간단한 다익스트라 알고리즘과 개선된 다익스트라 알고리즘 두가지 버전 중 개선된 코드를 다룬다.

전자는 O(V^2) 후자는 O(ElogV)의 복잡도를 가진다.

개선된 다익스트라 알고리즘에서는 우선순위 큐 사용을 위해 Heap 자료구조를 사용하며 파이썬에선 heapq 라이브러리가 이를 지원한다. 

우선순위 값을 표현할 때는 일반적으로 정수형 자료형의 변수가 사용되며 max,min heap여부에 따라 해당 큐가 나온다.(Max는 큰 값이, min은 낮은 데이터가 먼저 삭제 됨, 파이썬에서는 Min heap이 기반)

대부분의 프로그래밍 언어에서는 우선순위 큐에 데이터의 묶음을 넣으면 첫 번쨰 원소를 기준으로 우선순위를 결정한다.

```python
# 개선된 다익스트라 알고리즘 소스코드

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

#노드의 개수,간선
n,m=map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

#모든 간선 정보 입력
for _ in range(m):
    a,b,c=map(int,input().split())
    #a->b 로 cost가 c
    graph[a].append((b,c))

def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now=heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now]<dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost=dist+i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                
 for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
```

이는 O(ElogV)의 시간 복잡도를 가진다. 노드의 개수 V 이상의 횟수로는 반복되지 않고 V번 반복될 때 마다 연결된 E를 모두 확인하므로 ! 

힙에 N개의 데이터를 넣고 뺴는 과정은 O(NlogN)이고, 중복엣지를 포함하지 않는 경우 E는 항상  V**2 보다 작다.
$
O(logE)<O(logV^2)=O(2logV), 따라서 O(ElogV) 로 표현가능 
$


### 플로이드 워셜 알고리즘

모든 지점에서 다른 모든 지점까지의 최단 경로를 구해야 하는 경우 사용하는 알고리즘.
$$
단계마다 현재 노드를 거쳐가는 모든 경로를 고려한다, 따라서 N번 고려하면 O(N^3)의 시간 복잡도를 갖는다.
$$
노드의 개수가 N일 때, N번 만큼의 단계를 반복하며 '점화식'에 맞게 2차원 리스트를 갱신하기 때문에 DP라고 볼 수 있다.

각 단계에서는 해당 노드를 거쳐 가는 경우를 고려한다. 점화식은 아래와 같다. 
$$
D_(ab) = min(D_(ab),D_(ak) + D_(kb))
$$
즉 a에서b로 바로가거나 a에서 k를 들렸다 b로 가는 비용 중 더 작은 값으로 갱신한다.

전체적으로 (N-1)(N-2)개의 쌍을 단계마다 반복해서 확인하면 된다. 

```python
#플로이드 워셜 알고리즘 소스코드

노드 및 엣지의 수
n,m=map(int,input().split())
#2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph=[[]*(n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 코스트는 0 으로 초기화 
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0
            
#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    #A에서 B로 가는 비용은 C라고 설정
    a,b,c=map(int,input().split())
    graph[a][b]=c
    
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
            
# 결과 출력

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY",end=' ')
        else:
            print(graph[a][b],end=' ')
```



 우선순위 큐를 이용하는 다익스트라 알고리즘은 인접리스트랄 사용하는 방식이며, 플로이드 워셜 알고리즘은 인접 행렬을 이용하는 방식이다. 따라서 노드의 개수가 적은 경우 플로이드 워셜을 이용할 수 있으나 노드와 간선의 개수가 많은 경우 우선순위 큐를 이용하는 다익스트라 알고리즘을 사용하는 것이 유리하다. 

