import sys
from pprint import pprint
from itertools import permutations
import copy
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
# +, -, *, //
oper = list(map(int, input().split()))
min_value = int(1e10)
max_value = -int(1e10)

def get_oper_seq(oper):
    oper_arr = []
    for idx, value in enumerate(oper):
        oper_arr.extend([idx] * value)
    oper_seq = list(set(permutations(oper_arr, len(oper_arr))))
    return oper_seq

def caculate_equation(num, oper, idx):
    if oper == 0:
        num[idx+1] = num[idx] + num[idx + 1]
    elif oper == 1:
        num[idx+1] = num[idx] - num[idx+1]
    elif oper == 2:
        num[idx+1] = num[idx] * num[idx+1]
    else:
        if num[idx] < 0:
            num[idx+1] = -(-num[idx] // num[idx+1])
        else:
            num[idx+1] = num[idx] // num[idx+1]
    return num

def calculate_min(num, oper, idx, answer):
    global min_value, max_value
    if idx == len(num) - 1:
        if answer < min_value:
            min_value = answer
        if answer > max_value:
            max_value = answer
        return
    
    num = caculate_equation(num, oper[idx], idx)
    calculate_min(num, oper, idx + 1, num[idx+1])


oper_seq = get_oper_seq(oper)

for oper in oper_seq:
    num = copy.deepcopy(num_list)
    calculate_min(num, oper, 0, 0)
print(max_value)
print(min_value)