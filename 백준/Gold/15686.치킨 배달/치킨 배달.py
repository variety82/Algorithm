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
            tmp2.append(abs(choosen_chicken[i][k][0]-home[j][0])+\
                                  abs(choosen_chicken[i][k][1]-home[j][1]))
        tmp1.append(min(tmp2))
    chicken_Length.append(sum(tmp1))
print(min(chicken_Length))