deltas = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
new_dir = [0, 2, 1, 4, 3]


class Micro:
    def __init__(self, r, c, num, d):
        self.r = r
        self.c = c
        self.num = num
        self.d = d


def check(r, c):
    return r == 0 or r == N - 1 or c == 0 or c == N - 1


def move():
    info = {}
    for k in range(K):
        m = micros[k]
        if m.num == 0:
            continue
            
        m.r += deltas[m.d][0]
        m.c += deltas[m.d][1]
        
        if check(m.r, m.c):
            m.num //= 2
            m.d = new_dir[m.d]
            
        if (m.r, m.c) not in info.keys():
            info[(m.r, m.c)] = [k, m.num]
        else:
            pos, num = info[(m.r, m.c)]
            if m.num > num:
                info[(m.r, m.c)] = [k, m.num]
                m.num += micros[pos].num
                micros[pos].num = 0
            else:
                micros[pos].num += m.num
                m.num = 0
            micros[k] = m


def count_micros(arr):
    cnt = 0
    for m in arr:
        cnt += m.num
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    micros = []
    for _ in range(K):
        r, c, num, d = map(int, input().split())
        micros.append(Micro(r, c, num, d))
    for _ in range(M):
        move()
    ans = count_micros(micros)
    print(f"#{tc} {ans}")
