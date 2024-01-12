def solution(a, b, n):
    answer = 0
    while n >= a:
        q = n // a
        answer += (q * b)
        n = n - q * a + q * b
    return answer