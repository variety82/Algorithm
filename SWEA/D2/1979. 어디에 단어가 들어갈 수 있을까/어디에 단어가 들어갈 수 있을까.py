T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = []

    for i in range(n):
        cnt_row = 0
        cnt_col = 0
        for j in range(n):
            if arr[i][j] == 0:
                if cnt_row != 0:
                    answer.append(cnt_row)
                cnt_row = 0
            else:
                cnt_row +=1

            if arr[j][i] == 0:
                if cnt_col != 0:
                    answer.append(cnt_col)
                cnt_col = 0
            else:
                cnt_col +=1

        if cnt_row != 0:
            answer.append(cnt_row)
        if cnt_col != 0:
            answer.append(cnt_col)

    print(f"#{test_case} {answer.count(k)}")