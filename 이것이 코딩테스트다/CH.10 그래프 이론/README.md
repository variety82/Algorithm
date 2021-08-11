# 그래프 이론

___

### 서로소 집합 자료구조

- union

  두개의 집합을 하나로 합치는 연산

- find

  특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

서로소 집합 자료구조를 구현할 때는 트리 자료구조를 이용하여 집합을 표현한다.

알고리즘은 다음과 같다

1. union 연산을 확인하여, 서로 연결된 두 노드 A,B를 확인한다.

   1.1 A와 B의 루트 노드 A' , B' 을 각각 찾는다.

   1.2 A'을 B'의 부모 노드로 설정한다

1. 모든 union 연산을 처리할 때까지 1번의 과정을 반복한다.

초기 단계에서는 노드의 개수 크기의 부모 테이블을 초기화 한다. 이때 모든 원소가 자기 자신을 부모로 가지도록 설정한다. 여기서 유의할 점은 부모테이블엔 말 그대로 부모에 대한 정보만을 담고있어서 실제로 루트를 확인 할 때는 재귀적으로 거슬러 올라가 찾아야 한다.

```python
# 서로소 집합 알고리즘 소스코드

def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
```

그러나 위와 같은 경우 find함수가 최악의 경우 시간복잡도가 O(V)가 될 수 있다.

예를 들면, 

| 노드번호 | 1    | 2    | 3    | 4    | 5    |
| :------: | ---- | ---- | ---- | ---- | ---- |
|   부모   | 1    | 1    | 2    | 3    | 4    |

위와 같은 경우 1부터 5까지 모든 원소가 루트 노드로 1을 가지지만 순서대로 연결이 되어있어 5의 루트를 찾기 위해서는 순서대로 부모 노드를 거슬러 올라가야하므로 최대 O(V)의 시간이 소모된다.

이를 개선하기 위해 경로 압축 기법을 사용 할 수 있다, 경로 압축은 find 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 기법이다. 

```python
# 경로 압축 기법 소스코드
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
```

### 서로소 집합을 활용한 사이클 판별

서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용가능하다.

알고리즘은 아래와 같다.

1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
   1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다. 
   1. 루트 노드가 서로 같다면 사이크링 발생한 것이다. 
1. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

초기 단계에서는 모든 노드에 대하여 자기 자신을 부모로 설정하는 형태로 부모 테이블을 초기화 한다.

```python
cycle=False #싸이클 발생 여부
for i in range(e):
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break # 싸이클이 발생하면 종료
    else:
        union_parent(parent,a,b)
    
```

### 신장트리(Spanning Tree)

Def) 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

### 최소신장트리(Minimum Spanning Tree)

Def) Spanning Tree 중 최소 비용으로 만들 수 있는 트리

대표적으로 크루스칼 알고리즘을 사용하여  찾을 수 있다.

### 크루스칼 알고리즘(Kruskal Algorithm)

모든 엣지에 대해 정렬을 수행한 뒤 가장 거리가 짧은 엣지부터 집합에 포함시킨다. 이때 사이클을 발생시킬 수 있는 간선의 경우, 집합에 포함시키지 않는다. Greedy 알고리즘으로 분류되며 알고리즘은 아래와 같다.

1. Edge 데이터를 비용에 따라 오름차순으로 정렬한다.

1. Edge를 하나씩 확인하며 현재의 Edge가 사이클을 발생시키는지 확인한다.

   2.1 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.

   2.2 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.

1. 모든 엣지에 대해 2번의 과정을 반복한다.

```python
# 크루스칼 알고리즘 소스코드
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
#노드의 개수와 엣지(union 연산)의 개수 입력
v,e=map(int,input().split())
parent=[0]*(v+1) #부모테이블 초기화

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
result=0

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i
    
#모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
    
#엣지 정렬
edges.sort()

for edge in edges:
    cost,a,b=edge
    if(find_parent(parent,a)!=find_parent(parent,b)):
        union_parent(parent,a,b)
        result+=cost

```

크루스칼 알고리즘은 엣지의 개수가 E일 때 O(ElogE)의 시간 복잡도를 가진다. (엣지를 정렬하는 작업이 제일 오래걸려서!)



### 위상정렬(Topology Sort)

Def) 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용하는 알고리즘. 즉, 방향 그래프의 모든 노드를 '방향성에 어긋나지 않게 순서대로 나열하는 작업'

ex) 선수과목이 있는 학습순서 설정 

진입차수(Indegree) : 특정 노드로 들어오는 엣지의 개수

위상정렬의 알고리즘은 아래와 같다.

1. 진입차수가 0인 노드를 큐에 넣는다.

1. 큐가 빌 때까지 다음의 과정을 반복한다.

   1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.

   2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다. 

이때 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다, 사이클이 존재하는 경우 사이클에 포함되는 원소 중 어떠한 원소도 큐에 들어가지 못하기 때문이다. 

위상정렬의 특징으로는 위상정렬의 결과는 여러가지가 될 수 있다. 

```python
#위상 정렬 소스코드

from collection import deque
#노드,엣지 받기
v,e=map(int,input().split())
#모든 노드에 대한 진입차수 초기화
indegree=[0]*(v+1)
#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph=[[]for i in range(v+1)]

#방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1
    
def topology_sort():
    result=[] #알고리즘 수행결과를 담을 리스트
    q=deque()
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
            
    while q:
        now=q.popleft()
        result.append(now)
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i]-=1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i]==0:
                q.append(i)
```

위상정렬을 수행할 때는 차례대로 모든 노드를 확인해야하면서, 해당 노드에서 출발하느 간선을 차례대로 제거해야한다. 따라서, 위상정렬의 시간 복잡도는 O(V+E)이다. 
