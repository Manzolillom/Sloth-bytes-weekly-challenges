from seven_boom import  seven_boom

def test(lista, expRes):
    res = seven_boom(lista)
    if res != expRes:
        print(f"Test failed:\nInput: {lista}\nOutput: {res}\nExpected Output: {expRes}")
    else:
        print("Test Passed!")

test([1, 2, 3, 4, 5, 6, 7], "Boom!")

test([8, 6, 33, 100], "there is no 7 in the array")

test([2, 55, 60, 97, 86], "Boom!")

test([7, 77, 100], "Boom! Boom! Boom!")