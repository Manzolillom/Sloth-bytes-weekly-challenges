from day_of_year import dayOfYear

def test(sub: str, res:int):
    if(dayOfYear(sub) == res):
        print("Test passed")
    else:
        print(f"Test not passed on {sub}:\nResult: {dayOfYear(sub)}\nExpected: {res}\n---")

test("12/13/2020", 348)
# output = 348

test("11/16/2020", 321)
# output = 321

test("1/9/2019", 9)
# output = 9

test("3/1/2004", 61)
# output = 61

test("12/31/2000", 366)
# output = 366 # leap year

test("12/31/2019", 365)
# output = 365 #non leap year