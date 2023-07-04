import sys
input = sys.stdin.readline

answer = 0
while True:
    N = int(input())
    if N == -1:
        print(answer)
        break
    else:
        answer += N
