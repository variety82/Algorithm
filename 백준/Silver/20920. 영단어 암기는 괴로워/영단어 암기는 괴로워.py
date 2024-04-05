import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
word_dict = defaultdict(int)

for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    word_dict[word] += 1

word_dict = sorted(word_dict.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))

for word in word_dict:
    print(word[0])