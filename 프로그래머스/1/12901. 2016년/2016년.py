def solution(a, b):
    month_dict = {1:31, 2:29, 3:31 ,4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day_dict = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    day = -1
    for i in range(1, a):
        day += month_dict[i]
    day += b
    day %= 7
    return day_dict[day]