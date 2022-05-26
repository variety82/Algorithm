import datetime
T = int(input())

for ct in range(1, T+1):
    arr = input()
    year, month, day = arr[:4], arr[4:6], arr[6:]

    try:
        datetime.date(int(year), int(month), int(day))
        print(f"#{ct} {year}/{month}/{day}")
    except:
        print(f"#{ct} -1")