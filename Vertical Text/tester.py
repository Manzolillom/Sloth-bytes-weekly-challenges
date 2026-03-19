from vertical_txt import vertical_txt

def test(txt : str, expRes: list[list[chr]]):
    res = vertical_txt(txt)
    if res != expRes:
        print(f"Test failed:\nInput: {txt}\nOutput: {res}\nExpected Output: {expRes}")
    else:
        print("Test Passed!")

test("Holy bananas", (list[list[chr]])([["H", "b"],["o", "a"],["l", "n"],["y", "a"],[" ", "n"],[" ", "a"],[" ", "s"]]))

test("Hello fellas", (list[list[chr]])([["H", "f"],["e", "e"],["l", "l"],["l", "l"],["o", "a"],[" ", "s"]]))