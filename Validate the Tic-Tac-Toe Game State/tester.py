from validate_tic_tac_toe import validate

def test(txt : list[str], expRes: bool):
    res = validate(txt)
    if res != expRes:
        print(f"Test failed:\nInput: {txt}\nOutput: {res}\nExpected Output: {expRes}")
    else:
        print("Test Passed!")

test(["X  ", "   ", "   "], True)
test(["O  ", "   ", "   "], False)
test(["X X", " O ", "   "], True)
test(["XOX", " X ", "   "], False)
test(["XXX", "OO ", "   "], True) 
test(["XXX", "   ", "OOO"], False)