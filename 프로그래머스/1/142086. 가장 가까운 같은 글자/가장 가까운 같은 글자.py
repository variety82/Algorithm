from collections import defaultdict
def solution(s):
    answer = [0] * len(s)
    word_dict = defaultdict(int)

    for idx, spelling in enumerate(s):
        if word_dict.get(spelling) == None:
            word_dict[spelling] = idx
            answer[idx] = -1
        else:
            answer[idx] = idx - word_dict[spelling]
            word_dict[spelling] = idx

    return answer