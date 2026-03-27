def solve_daily_temp(temperatures: list[int], current:int, jump:int, size:int , output: list[int]) -> int:
    if temperatures[current] < temperatures[current+jump]:
        return jump
    if jump+current > size or output[current+jump] == 0:
        return 0
    return solve_daily_temp(temperatures, current, jump+output[current+jump], size, output)

def daily_temperatures(temperatures: list[int]) -> list[int]:
    size = len(temperatures)
    output = [0 for x in range(0, size)]
    for x in range(size-2, -1, -1):
        output[x] = solve_daily_temp(temperatures, x, 1, size-1, output)
    return output