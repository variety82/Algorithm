import math
N = int(input())

def isPrime(n):
    n = int(n)
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def findPrime(n):
    if(len(n) == N):
        print(n)
        return
    for num in ['1', '3', '7', '9']:
        if isPrime(n + num):
            findPrime(n + num)


for num in ['2', '3', '5', '7']:
    findPrime(num)