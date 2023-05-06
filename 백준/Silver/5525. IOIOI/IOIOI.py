import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
answer = 0

P = ""
for i in range(N * 2 + 1):
    if(i % 2 == 0):
        P += "I"
    else:
        P += "O"
start = 0
end = len(P)

while(end != M + 1):
    if(S[start:end] == P):
        answer += 1
    start += 1
    end += 1

print(answer)

