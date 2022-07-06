#import sys

T = int(input())

for test_case in range(1, T + 1):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) > len(B):
        A, B = B, A
    answer = 0
  
    for i in range(len(B)-len(A)+1):
        tmp = 0
        for j in range(len(A)):
            tmp += A[j] * B[j+i]
        answer = max(answer, tmp)
    print(f"#{test_case} {answer}")