import sys
from pprint import pprint
from itertools import permutations
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
# +, -, *, //
oper = list(map(int, input().split()))
min_value = int(1e10)
max_value = -int(1e10)
def dfs(answer, idx, plus, minus, multiply, divide):
    global max_value, min_value
    if idx == len(num_list):
        max_value = max(max_value, answer)
        min_value = min(min_value, answer)
        return
    
    if plus:
        dfs(answer + num_list[idx], idx + 1, plus - 1, minus, multiply, divide)
    if minus:
        dfs(answer - num_list[idx], idx + 1, plus, minus - 1, multiply, divide)
    if multiply:
        dfs(answer * num_list[idx], idx + 1, plus, minus, multiply - 1, divide)
    if divide:
        dfs(int(answer / num_list[idx]), idx + 1, plus, minus, multiply, divide - 1)

dfs(num_list[0], 1, oper[0], oper[1], oper[2], oper[3])
print(max_value)
print(min_value)