from itertools import combinations
N = int(input())
min_val = float("INF")
soccer = [list(map(int, input().split())) for _ in range(N)] 
candidate = list(combinations(range(N), N // 2))
start = []

for candi in candidate:
    start.append([x for x in list(range(N)) if x not in candi])
for c, s in zip(candidate, start):
    cc = list(combinations(c, 2))
    ss = list(combinations(s, 2))
    c_candi = 0
    s_candi = 0
    for ccc, sss in zip(cc, ss):
        c_candi += soccer[ccc[0]][ccc[1]]
        c_candi += soccer[ccc[1]][ccc[0]]
        s_candi += soccer[sss[0]][sss[1]]
        s_candi += soccer[sss[1]][sss[0]]

    temp = abs(c_candi - s_candi)
    min_val = min(min_val, temp)
print(min_val)