import sys
input = sys.stdin.readline

N = int(input())

idx_map = {0 : 5, 5 : 0, 1 :3, 3 : 1, 2 : 4, 4 : 2}
dices = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def find_idx(num, dice):
    idx = dice.index(num)
    next_num = dice[idx_map[idx]]
    return idx, next_num

for i in range(1, 7):
    cnt = 0
    next_num = i
    for dice in dices:
        idx, next_num = find_idx(next_num, dice)
        if(idx == 0 or idx == 5):
            cnt += max(dice[1], dice[2], dice[3], dice[4])
        elif(idx == 1 or idx == 3):
            cnt += max(dice[0], dice[2], dice[4], dice[5])
        else:
            cnt += max(dice[0], dice[1], dice[3], dice[5])
    answer = max(answer, cnt)

print(answer)
