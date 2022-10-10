from pprint import pprint
# from copy import deepcopy
import copy
from collections import deque
from itertools import product
deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())

def is_in(r, c):
    global H, W
    return r >= 0 and r < H and c >= 0 and c < W

def boom(arr, r, c):
    q = deque()
    #  벽돌 있떤 자리를 0을 변경해서 방문처리
    if(arr[r][c] > 1):
        q.append([r, c, arr[r][c]])
    arr[r][c] = 0

    while(q):
        point = q.popleft()
        cnt = point[2]
        for d in range(4):
            #  현재 방향에서 cnt - 1만큼 벽돌깨기 
            nr = point[0]
            nc = point[1]
            for k in range(1, cnt):
                nr += deltas[d][0]
                nc += deltas[d][1]
                if(is_in(nr, nc) and arr[nr][nc] > 0):
                    if(arr[nr][nc] > 1):
                        q.append([nr, nc, arr[nr][nc]])
                    arr[nr][nc] = 0
    
def down(arr):
    global W, H
    for c in range(W):
        stack = []
        for r in range(H):
            if(arr[r][c] > 0):
                stack.append(arr[r][c])
                arr[r][c] = 0
        nr = H - 1
        while(stack):
            arr[nr][c] = stack.pop()
            nr -= 1


def get_remain(arr):
    global H, W
    cnt = 0
    for r in range(H):
        for c in range(W):
            if(arr[r][c] > 0):
                cnt += 1
    return cnt
        
def game(arr, cnt, beads):
    global min_val, W, H, N
    for bead in beads:
        r = 0
        while(r < H and arr[r][bead] == 0):
            r += 1
        if(r == H):
            continue
        else:
            boom(arr, r, bead)
            down(arr)
            cnt += 1

    min_val = min(min_val, get_remain(arr))
    return

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    beads = list(product(range(W), repeat = N))
    min_val = 100000000
    for bead in beads:
        arr = copy.deepcopy(board)
        game(arr, 0, bead)
    print(f"#{tc} {min_val}")
    

