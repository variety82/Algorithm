def solution(n):
    return int("".join(sorted([x for x in list(str(n))], reverse=True)))