import sys
import heapq
input = sys.stdin.readline

N = int(input())
students = [list(map(int, input().split())) for _ in range(N * N)]
students_dict = {}
score_dict = {0:0, 1:1, 2:10, 3:100, 4:1000}
for student in students:
    students_dict[student[0]] = student[1:]

graph = [[0] * N for _ in range(N)]
deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def is_in(r, c):
    return 0 <= r < N and 0 <= c < N

def calculate_around_info(r, c, favorite_member):
    around_sum = 0
    empty_score = 0
    for i in range(4):
        nr = r + deltas[i][0]
        nc = c + deltas[i][1]
        if not is_in(nr, nc):
            continue
        if graph[nr][nc] in favorite_member:
            around_sum += 1
        if graph[nr][nc] == 0:
            empty_score += 1
    return around_sum, empty_score

def serach(favorite_member):
    q = []
    for r in range(N):
        for c in range(N):
            if graph[r][c] != 0:
                continue
            around_sum, empty_score = calculate_around_info(r, c, favorite_member)
            heapq.heappush(q, (-around_sum, -empty_score, (r, c)))
    return heapq.heappop(q)

def caculate_answer():
    score = 0
    for r in range(N):
        for c in range(N):
            cnt = 0
            for i in range(4):
                nr = r + deltas[i][0]
                nc = c + deltas[i][1]
                if not is_in(nr, nc):
                    continue
                if graph[nr][nc] in students_dict[graph[r][c]]:
                    cnt += 1
            score += score_dict[cnt]
    return score

for student in students:
    member = student[0]
    favorite_member = student[1:]
    _, _, (nr, nc) = serach(favorite_member)
    graph[nr][nc] = member
    
print(caculate_answer())