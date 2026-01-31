import re

MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year : int) -> bool:
    return (year%400 == 0 or (year%4 == 0 and year%100 != 0))

def dayOfYear(data : str) -> bool:
    # Using regex to separate the numbers in a simpler way (imo)
    dateRe = re.compile(r'(\d+)/(\d+)/(\d+)')
    mo = dateRe.search(data)
    if mo == None:
        print("Error in data structure")
        return False

    # mm/dd/yyyy date format </3
    month = int(mo.group(1))
    day = int(mo.group(2))
    year = int(mo.group(3))

    result = day # it starts with the day and then adds up the rest
    # Checks for leap year
    if is_leap_year(year) and month > 2:
        result = result + 1
    for days in MONTHS[:(month-1)]:
        result += days
    return result