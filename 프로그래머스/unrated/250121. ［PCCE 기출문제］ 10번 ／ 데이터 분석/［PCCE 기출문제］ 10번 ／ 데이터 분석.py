def sort_by_ext(data, ext, val_ext):
    idx = -1
    if ext == 'code':
        idx = 0
    elif ext == 'date':
        idx = 1
    elif ext == 'maximum':
        idx = 2
    else:
        idx = 3
    data.sort(key = lambda x : x[idx])
    for cur_idx, value in enumerate(data):
        if value[idx] > val_ext:
            return data[:cur_idx]

def sort_by_str(data, sort_by):
    idx = -1
    if sort_by == 'code':
        idx = 0
    elif sort_by == 'date':
        idx = 1
    elif sort_by == 'maximum':
        idx = 2
    else:
        idx = 3
    return sorted(data, key = lambda x : x[idx])

def solution(data, ext, val_ext, sort_by):
    data = sort_by_ext(data, ext, val_ext)
    data = sort_by_str(data, sort_by)
    return data