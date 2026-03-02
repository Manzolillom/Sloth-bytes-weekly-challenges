# Seven boom

def count_sevens(num : int) -> int:
    if num/10 == 0:
        return 0
    if num%10 == 7 :
        return count_sevens(int(num/10)) + 1
    else:
        return count_sevens(int(num/10))

def seven_boom(num : list[int]) -> str:
    stringa = ""
    for n in num:
        stringa += count_sevens(n) * "Boom! "
    if stringa == "":
        return "there is no 7 in the array"
    return stringa.removesuffix(" ")