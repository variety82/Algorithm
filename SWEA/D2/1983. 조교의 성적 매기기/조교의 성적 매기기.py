T = int(input())

score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for tc in range(1, T+1):
    total_score = []
    n, k = map(int, input().split())
    _max = n//10 # 성적을 최대 몇명이 받을 수 있는지 
    for idx in range(n):
        m, f, a = map(int, input().split()) #mid, final, assingment 약자
        total_score.append((idx + 1, (m * 0.35 + f * 0.45 + a * 0.2)))
        total_score.sort(reverse=True, key = lambda x : x[1])
    tmp = [x[0] for x in total_score]  # 학생 번호 조회를 위한 과정, 위에서 정렬해놨기에 점수가 높은순으로 들어감 

    # 성적을 받을 수 있는 학생 수 만큼 나눠줌(계속 빼는 역할)
    print(f"#{tc} {score[(tmp.index(k)) // _max]}")