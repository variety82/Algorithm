
def solution(s):
    answer = ''
    s_length = len(s)
    if s_length % 2 == 1:
        return s[s_length // 2]
    else:
        return s[(s_length // 2) - 1 : s_length // 2 + 1]