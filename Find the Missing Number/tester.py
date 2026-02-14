from missing_num import missingNum

def test(arr, oracle):
    result = missingNum(arr)
    if result == oracle:
        print(f"Test passato!")
    else:
        print(f"Failed test\nInput: {arr}\nOutput: {result}\nExpected: {oracle}")

test([1, 2, 3, 4, 6, 7, 8, 9, 10],5)
test([7, 2, 3, 6, 5, 9, 1, 4, 8],10)
test([10, 5, 1, 2, 4, 6, 8, 3, 9], 7)