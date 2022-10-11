def make_road(road):
    size, j = 0, 0
    pre_height = road[0]
    while(j < N):
        # 같을 때
        if(pre_height == road[j]):
            size += 1
            j += 1
        # 높아질 때
        elif(pre_height + 1 == road[j]):
            if(size < L):
                return False
            pre_height += 1
            j += 1
            size = 1
        # 낮아질 때
        elif(pre_height - 1 == road[j]):
            cnt = 0
            for k in range(j, N):
                if(pre_height - 1 != road[k]):
                    return False
                cnt += 1
                if(cnt == L):
                    break
            if(cnt < L):
                return False
            pre_height -= 1
            j += L
            size = 0

        else:
            return False
    return True

def count_road():
    ans = 0
    for r in range(N):
        if(make_road(vertical[r])):
            ans += 1
        if(make_road(horizon[r])):
            ans += 1
    return ans

def make_vertical(horizon):
    vertical = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            vertical[r][c] = horizon[c][r]
    return vertical


N, L = map(int, input().split())
horizon = [list(map(int, input().split())) for _ in range(N)]
vertical = make_vertical(horizon)

ans = count_road()

print(ans)
