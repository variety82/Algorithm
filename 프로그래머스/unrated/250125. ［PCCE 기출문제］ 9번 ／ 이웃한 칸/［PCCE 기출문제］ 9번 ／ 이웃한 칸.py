deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def is_in(N, M, r, c):
    return 0 <= r < N and 0 <= c < M

def solution(board, h, w):
    answer = 0
    color = board[h][w]
    N = len(board)
    M = len(board[0])
    for delta in deltas:
        nr = h + delta[0]
        nc = w + delta[1]
        if not is_in(N, M, nr, nc):
            continue
        if board[nr][nc] == color:
            answer += 1
    return answer
