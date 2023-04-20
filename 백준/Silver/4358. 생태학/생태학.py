import sys
from collections import Counter
lines = sys.stdin.readlines()

arr = []
arr_set = {}
total_num = 0
for line in lines:
    total_num += 1
    arr.append(line.rstrip())

arr_set = sorted(set(arr))
arr = Counter(arr)

for element in arr_set:
    print(f"{element} {((arr[element] / total_num) * 100):.4f}")