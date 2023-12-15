
from collections import defaultdict
def solution(keymap, targets):
    key_dict = defaultdict(int)
    answer = []
    for key in keymap:
        for idx, k in enumerate(key):
            if key_dict[k] == 0:
                key_dict[k] = idx + 1
            elif key_dict[k] > idx + 1:
                key_dict[k] = idx + 1

    for target in targets:
        num = 0
        for t in target:
            if key_dict[t] == 0:
                answer.append(-1)
                break
            else:
                num += key_dict[t]
        else:
            answer.append(num)
    return answer