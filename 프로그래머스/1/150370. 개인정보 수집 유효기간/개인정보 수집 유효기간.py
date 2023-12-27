def caclulate_date(today, privacie, terms_dict):
    date, kind = privacie.split()
    expiration_date = terms_dict[kind]
    year, month, day = map(int, date.split("."))
    q, r = divmod(month + expiration_date, 12)
    if (month + expiration_date) % 12 == 0:
        q -= 1
    year += q
    month = r if r != 0 else 12
    if day - 1 == 0:
        if month - 1 == 0:
            year -= 1
            month = 12
        else:
            month -= 1
        day = 28
    else:
        day -= 1
    today_year, today_month, today_day = map(int, today.split("."))
    if today_year > year:
        return False
    if today_year == year and today_month > month:
        return False
    if today_year == year and today_month == month and today_day > day:
        return False
    return True

def terms_arr_to_dict(terms):
    terms_dict = {}
    for term in terms:
        kind, num = term.split()
        terms_dict[kind] = int(num)
    return terms_dict


def solution(today, terms, privacies):
    answer = []
    terms_dict = terms_arr_to_dict(terms)
    for idx, privacie in enumerate(privacies):
        if not caclulate_date(today, privacie, terms_dict):
            answer.append(idx + 1)
    return answer