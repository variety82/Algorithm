from pprint import pprint

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
airCon = []

for r in range(R):
    for c in range(C):
        if(arr[r][c] == -1):
            airCon.append([r, c + 1])

def isIn(r : int, c : int) -> bool:
    if(r >= 0 and r < R and c >= 0 and c < C):
        return (arr[r][c] != -1)
    else:
        return False

def moveDust() -> None:
    global arr
    temp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if(arr[r][c] == -1):
                continue
            cnt = 0
            for i in range(4):
                nr = r + deltas[i][0]
                nc = c + deltas[i][1]
                if(not isIn(nr, nc)):
                    continue
                temp[nr][nc] += (arr[r][c] // 5)
                cnt += 1
            arr[r][c] -= (arr[r][c] // 5) * cnt
    for r in range(R):
        for c in range(C):
            arr[r][c] += temp[r][c]

def makeWind() -> None:
    ur, uc = airCon[0]
    dr, dc = airCon[1]
    #하
    for r in range(ur, 0, -1):
        if(arr[r][0] == -1):
            continue
        arr[r][0] = arr[r - 1][0]
    # 좌
    for c in range(0, C-1, 1):
        arr[0][c] = arr[0][c + 1]

    # 상
    for r in range(0, ur, 1):
        arr[r][C - 1] = arr[r + 1][C - 1]

    # 우
    for c in range(C - 1, 1, -1):
        arr[ur][c] = arr[ur][c - 1]
    arr[ur][1] = 0

    # 상
    for r in range(dr, R - 1, 1):
        if(arr[r][0] == -1):
            continue
        arr[r][0] = arr[r + 1][0]

    # 좌
    for c in range(0, C - 1, 1):
        arr[R - 1][c] = arr[R - 1][c + 1]

    # 하
    for r in range(R - 1, dr, -1):
        arr[r][C - 1] = arr[r - 1][C - 1]

    # 우
    for c in range(C - 1, 1, -1):
        arr[dr][c] = arr[dr][c - 1]
    arr[dr][1] = 0

for _ in range(T):
    moveDust()
    makeWind()
answer = 0
for i in range(R):
    answer += sum(arr[i])
print(answer + 2)