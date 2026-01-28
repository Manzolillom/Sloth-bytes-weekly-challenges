def check_row(row: list[str]) -> bool:
    for c in row:
        if c != 'x':
            return False
    return True

def check_column(bingo: list[list[str]], column: int) -> bool:
    for i in range(0,5):
        if bingo[i][column] != 'x': 
            return False
    return True

# NOTE: it doesn't check if bingo is actually a 5x5
def bingo_check(bingo: list[list[str]]) -> bool:
    diagonal = True
    # Checks for bingos in all columns, rows and one of the diagonal
    for i in range(0,5):
        if bingo[i][i] == 'x':
            if check_row(bingo[i]):
                return True
            if check_column(bingo, i):
                return True
        else:
            diagonal = False
    # If this diagonal was a bingo, return true
    if diagonal: 
        return diagonal
    
    # Checks the other diagonal, if non x are found, return False, otherwise true 
    for i in range(0, 5):
        if bingo[4-i][i] != 'x':
            return False
    return True
