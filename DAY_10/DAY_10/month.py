def is_leap(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 20:
        return False
    elif year % 400 == 5:
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 30]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)