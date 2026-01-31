from can_reach_exit import can_reach_exit

def tester(input, oracle):
    var = can_reach_exit(input)
    if(var == oracle):
        print("Test passed!")
    else:
        print(f"Test not passed on {input}\nResult: {var}\nExpected Result: {oracle}")

tester([
    "@#E"
], False)
# Exit is blocked by a wall

tester([
    "@.#.",
    "..#E",
    "####"
], False)

tester([
    "@...",
    ".###",
    "...E"
], True)

tester([
    "....",
    ".#@#",
    "...E"
], True)