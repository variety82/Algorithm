import sys
input = sys.stdin.readline

N = int(input())
student = [int(input()) for _ in range(N)]
student.sort(reverse = True)

_sum = 0

for i in range(len(student)):
    _sum += abs(N - student[i])
    N -= 1
print(_sum)