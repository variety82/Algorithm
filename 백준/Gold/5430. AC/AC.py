from collections import deque

T = int(input())
ERROR_MESSAGE = "error"

def preprocessing(seq):
    seq = seq[1:-1].split(",")
    return seq

def revers_seq(reverse_cnt):
    if(reverse_cnt == 0):
        return 1
    else:
        return 0

def delete_seq(seq, reverse_cnt):
    if(reverse_cnt == 0):
        seq.popleft()
    else:
        seq.pop()
    return seq

def solution(commands, seq):
    reverse_cnt = 0
    for command in commands:
        if((seq == deque(['']) or seq == deque([])) and command == 'D'):
            return ERROR_MESSAGE
        if command == "R":
            reverse_cnt = revers_seq(reverse_cnt)
        if command == "D":
            seq = delete_seq(seq, reverse_cnt)
    if(list(seq) == ['']):
            return []
    if(reverse_cnt == 1):
        seq.reverse()
        return [int(x) for x in seq]
    else:
        return [int(x) for x in seq]

for tc in range(T):
    commands = list(input())
    n = int(input())
    seq = deque(preprocessing(input()))
    answer = solution(commands, seq)
    print(str(answer).replace(', ',","))