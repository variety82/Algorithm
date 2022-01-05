'''
2021-11-11 : BOJ 15686

idea: 조합으로 선택가능한 치킨집을 선택한다, 그 후 각 집마다 치킨거리를 구한다
각 집마다 모두 구했으면 도시의 치킨거리를 구한후 그 중 제일 작은 것을 선택
'''
from itertools import combinations
import math
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

chicken = []
home = []
chicken_Length = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i,j))
            
        if arr[i][j] == 1:
            home.append((i,j))

home_Len = len(home)
chicken_cnt = len(chicken)
cnt = math.factorial(chicken_cnt) // (math.factorial(m)*math.factorial(chicken_cnt-m))

choosen_chicken = list(combinations(chicken, m))

#조합으로 선택가능한 치킨 집 선택후, 집 하나당 치킨거리(tmp2) 계산, 그후 모든집 치킨거리 계산후 도시의 치킨거리 저장


for i in range(cnt):
    tmp1 = []
    for j in range(home_Len):
        tmp2 = []
        for k in range(m):
            tmp2.append(abs(choosen_chicken[i][k][0]-home[j][0])+                                  abs(choosen_chicken[i][k][1]-home[j][1]))
        tmp1.append(min(tmp2))
    chicken_Length.append(sum(tmp1))
print(min(chicken_Length))

'''
회고 1 : i,j,k 인덱스 때문에 뻘짓을 너무 많이 했다.. 순서를 잘 생각하자...
, 채점돌릴 때 계속 런타임오류(네임 에러)가 났는데 셀 밑에 쳐놓고 정작 채점할 떄는 빼먹었다..
'''

