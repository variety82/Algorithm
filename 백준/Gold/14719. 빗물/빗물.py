

n, m = map(int, input().split())
block = [[0] * m for _ in range(n)]
block_height = list(map(int, input().split()))
# pprint(block_height)
def init_block():
    for c in range(m):
        for r in range(block_height[c]):
            block[n-r-1][c] = 1

def is_fill(height, width):
    left = False
    right = False
    if(block[height][width] == 1):
        return False
    for l in range(width):
        if(block[height][l] == 1):
            left = True
            break;
    for r in range(width, m):
        if(block[height][r] == 1):
            right = True
            break;
    return left and right


def fill_block():
    cnt = 0
    for r in range(n):
        for c in range(m):
            if(is_fill(r, c)):
                block[r][c] = 2
                cnt += 1
    return cnt



init_block()
print(fill_block())