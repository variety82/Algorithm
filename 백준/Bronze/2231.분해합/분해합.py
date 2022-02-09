n = int(input())

arr = []
test = list(range(1, n + 1))[::-1]

for i in range(len(test)):
    if test[i] + sum([int(x) for x in str(test[i])]) == n:
        arr.append(test[i])
    else:
        continue
if len(arr) == 0:
    print(0)
else:
    print(min(arr))