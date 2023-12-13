def solution(data, ext, val_ext, sort_by):
    answer = []
    case = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    for single_data in data:
        if single_data[case.get(ext)] < val_ext:
            answer.append(single_data)
    return sorted(answer, key = lambda x :x[case.get(sort_by)])