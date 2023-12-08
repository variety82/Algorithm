deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def is_in(r, c, N, M):
    return 0 <= r < N and 0 <= c < M


def solution(park, routes):
    N = len(park)
    M = len(park[0])
    for r in range(N):
        for c in range(M):
            if park[r][c] == 'S':
                pos = [r, c]
                break

    for route in routes:
        dir, dist = route.split()
        flag = True
        for i in range(int(dist) + 1):
            if dir == 'N':
                nr = pos[0] + deltas[0][0] * i
                nc = pos[1] + deltas[0][1] * i
            elif dir == 'S':
                nr = pos[0] + deltas[1][0] * i
                nc = pos[1] + deltas[1][1] * i
            elif dir == 'W':
                nr = pos[0] + deltas[2][0] * i
                nc = pos[1] + deltas[2][1] * i
            else:
                nr = pos[0] + deltas[3][0] * i
                nc = pos[1] + deltas[3][1] * i
            if not is_in(nr, nc, N, M):
                flag = False
                break
            if park[nr][nc] == 'X':
                flag = False
                break
        if flag:
            pos = [nr, nc]

    return pos