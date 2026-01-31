from how_many_missing import howManyMissing

def test(lista, expRes):
    res = howManyMissing(lista)
    if res != expRes:
        print(f"Test failed:\nInput: {lista}\nOutput: {res}\nExpected Output: {expRes}")
    else:
        print("Test Passed!")

test([1, 2, 3, 8, 9], 4)
output = 4
# The numbers missing from this line are 4, 5, 6, and 7.
# 4 numbers are missing.
test([1, 3], 1)
# output = 1

test([7, 10, 11, 12], 2)
# output = 2

test([1, 3, 5, 7, 9, 11], 5)
# output = 5

test([5, 6, 7, 8], 0)
# output = 0