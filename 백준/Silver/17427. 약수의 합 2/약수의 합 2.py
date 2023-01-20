N = int(input())
# n까지의 수에서 i약수로 표현할 수 있는 갯수가 n // k
answer = sum(i * (N // i) for i in range(1, N + 1))
print(answer)