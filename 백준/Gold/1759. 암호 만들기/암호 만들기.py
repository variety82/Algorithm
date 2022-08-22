from itertools import combinations

L, C = map(int, input().split())
arr = list(map(str, input().split()))
vowel = [x for x in arr if x in ["a", "e", "i", "o", "u"]]
consonant = [x for x in arr if x not in ["a", "e", "i", "o", "u"]]
answer = []

def makePw():
    global L
    cnt = 0
    for i in range(1, L - 2 + 1):
        vow = list(combinations(vowel, i))
        con = list(combinations(consonant, L - i))
        for v in vow:
            for c in con:
                answer.append(v + c)
makePw()

for i in range(len(answer)):
    answer[i] = sorted(answer[i])
    answer[i] = "".join(answer[i])
    
answer.sort()
for i in range(len(answer)):
    print(answer[i])