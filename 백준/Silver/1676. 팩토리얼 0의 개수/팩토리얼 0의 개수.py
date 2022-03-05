import math as m
n = int(input())
num = str(m.factorial(n))

idx = -1
cnt = 0

flag = True
while flag:
    if num[idx] == '0':
        cnt += 1
        idx -= 1
    else:
        break

print(cnt)