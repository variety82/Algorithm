n, s = map(int, input().split())
arr = [int(x) for x in input().split()]

k = int(1e9)
end = 0
interval_sum = 0

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += arr[end]
        end += 1
#     print('strat:',start,'end:',end)
#     print(interval_sum)
    if interval_sum >= s:
        k = min(k, end - start)
    interval_sum -= arr[start]
print(0) if k == int(1e9) else print(k)