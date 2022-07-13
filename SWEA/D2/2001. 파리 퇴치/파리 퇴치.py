T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    k = n - m + 1
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_fly = 0
    start_col = 0

    for i in range(k):
        start_row = 0

        for j in range(k):
            sum_fly = 0

            for l in range(m):
                sum_fly += sum(arr[l + start_col][start_row:start_row + m])
            start_row += 1
            max_fly = max(max_fly, sum_fly)
        start_col += 1
        
    print(f"#{test_case} {max_fly}")