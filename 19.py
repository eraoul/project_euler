
from timeit import timeit

def is_leap_year(y):
    return (y%4 == 0) and (y%400 == 0 or y%100 != 0)

@timeit
def solution():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day_of_week = 1  # Monday
    day = 1
    month = 0  # Jan
    year = 1900

    count = 0
    while year < 2001:
        if day == 1 and day_of_week == 0 and year > 1900:  # Sunday 1st of month, starting 1901
            count += 1
        day_of_week = (day_of_week+1) % 7
        if month == 1 and day == 28 and is_leap_year(year):
            day = 29
        else:
            day+=1
            if day > days_in_month[month]:
                day = 1
                month += 1
                if month == 12:
                    month = 0
                    year += 1
    print count

solution()
