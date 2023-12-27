def time_to_day(date):
    year, month, day = map(int, date.split("."))
    return year * 12 * 28 + month * 28 + day

def terms_arr_to_dict(terms):
    terms_dict = {}
    for term in terms:
        kind, num = term.split()
        terms_dict[kind] = int(num) * 28
    return terms_dict

def solution(today, terms, privacies):
    answer = []
    terms_dict = terms_arr_to_dict(terms)
    today = time_to_day(today)
    for idx, privacy in enumerate(privacies):
        date, kind = privacy.split()
        expiration_date = time_to_day(date) + terms_dict[kind]
        if expiration_date <= today:
            answer.append(idx + 1)
    return answer