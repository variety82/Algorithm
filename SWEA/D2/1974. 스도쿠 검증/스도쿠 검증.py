T = int(input())


for test_case in range(1, T + 1):
    sdocu = [list(map(int, input().split())) for _ in range(9)]

    check_v =[0] * 9
    check_h =[0] * 9
    check = []

    for i in range(9):
        if sum(sdocu[i]) == 45:
            check_h[i] = True
        else:
            check_h[i] = False
    
    for i in range(9):
        check_sum = 0
        for j in range(9):
            check_sum += sdocu[j][i]
        if check_sum == 45:
            check_v[i] = True
        else:
            check_v[i] = False

    for i in range(0, 9, 3):
        check_sum = 0
        cnt = 0
        for j in range(9):
            cnt += 1 
            check_sum += sum(sdocu[j][i:i+3])
            if cnt == 3:
                if check_sum == 45:
                    check.append(True)
                else:
                    check.append(False)
                cnt = 0
                check_sum = 0

    # print(check_h, check_v, check)
    if (False in check_h or False in check_v or False in check) == False:
        print(f"#{test_case} {1}")
    else:
        print(f"#{test_case} {0}")
