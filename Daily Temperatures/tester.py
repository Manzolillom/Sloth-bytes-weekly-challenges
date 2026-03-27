from daily_temperatures import daily_temperatures

f = daily_temperatures

def test(input , expRes):
    res = f(input)
    if res != expRes:
        print(f"Test failed:\nInput: {input}\nOutput: {res}\nExpected Output: {expRes}")
    else:
        print("Test Passed!")

test([30,38,30,36,35,40,28], [1,4,1,2,1,0,0])
test([22,21,20], [0,0,0])
