def solution(s):
    number_idct = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
    for v in number_idct:
        s = s.replace(v, str(number_idct[v]))
    return int(s)