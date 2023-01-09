def split_seq(string, length):
    candidates = []
    for i in range(len(string) - length + 1):
        candidates.append(int(string[i:i+length]))
    return candidates


def count_subseq(candidates, seq):
    cnt = 0
    for candidate in candidates:
        if(candidate <= seq):
            cnt += 1
    return cnt

def solution(t, p):
    seq_length = len(p)
    p = int(p)
    candidates = split_seq(t, seq_length)

    return count_subseq(candidates, p)