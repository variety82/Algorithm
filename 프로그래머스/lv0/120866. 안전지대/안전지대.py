deltas = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]


def solution(board):
    N = len(board)
    boom = [[0] * N for _ in range(N)]
    
    def is_in(r, c):
        return 0 <= r < N and 0 <= c < N


    def count_safe_zone():
        cnt = 0
        for r in range(N):
            for c in range(N):
                if(boom[r][c] == 0):
                    cnt += 1
        return cnt
    
    
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                boom[r][c] = -1
                for d in deltas:
                    nr = r + d[0]
                    nc = c + d[1]
                    if(is_in(nr, nc)):
                        boom[nr][nc] = -1
    answer = count_safe_zone()
                          
    return answer