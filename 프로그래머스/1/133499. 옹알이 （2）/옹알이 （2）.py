def solution(babbling):
    word_list = ["aya", "ye", "woo", "ma"]
    answer = 0
    for babb in babbling:
        for word in word_list:
            if word * 2 not in babb:
                babb = babb.replace(word, ' ')
        if len(babb.strip()) == 0:
            answer += 1
    return answer