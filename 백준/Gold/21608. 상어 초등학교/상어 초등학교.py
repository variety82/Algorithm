import sys
from pprint import pprint
import heapq
input = sys.stdin.readline

N = int(input())
students = [list(map(int, input().split())) for _ in range(N * N)]
students_dict = {}

for student in students:
    students_dict[student[0]] = student[1:]


graph = [[0] * N for _ in range(N)]
deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# 그래프를 탐색하면서 좋아하는 학생이 많은 칸에 앉아야 됨
# 그런 칸이 여러개면 인접한 칸 중 비어있는 칸이 제일 많은 곳을 선택(조건 2)
# 조건2 까지 동일할 경우 행이 가장 작은 곳으로, 두 번째는 열이 가장 작은 곳으로
        
# 우선순위 큐에 넣어? (-좋아하는 학생 수, -비어있는 칸 수, (r, c)), 기본적으로 min heap이니까 앞에 두 개는 max heap처리
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
    return q

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
            if cnt == 1:
                score += 1
            elif cnt == 2:
                score += 10
            elif cnt == 3:
                score += 100
            elif cnt == 4:
                score += 1000
    return score

for student in students:
    member = student[0]
    favorite_member = student[1:]
    q = serach(favorite_member)
    _, _, (nr, nc) = heapq.heappop(q)
    graph[nr][nc] = member
print(caculate_answer())