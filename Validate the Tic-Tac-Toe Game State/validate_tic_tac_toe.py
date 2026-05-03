import re

def count_wins(matrix : list[list[str]]) -> int: # I couldn't figure out a good way to do this :((
    wins = 0
    for i in range(0,3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != ' ':
            wins+=1
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != ' ':
            wins+=1
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != ' ':
        wins += 1
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != ' ':
        wins += 1
    return wins

def validate(input : list[str]) -> bool:
    matrix = [["" for _ in range(3)] for _ in range(3)]
    rowRegex = re.compile(r"([XO ])([XO ])([XO ])")
    nCircle = 0
    nCross = 0

    i = 0
    for riga in input:
        mo = rowRegex.search(riga)
        for j in range(1, 4):
            matrix[j-1][i] = mo.group(j) # Add character to matrix
            if mo.group(j) == "X": # if it's an X remember there's an X more in the playing grid
                nCross += 1
            if mo.group(j) == "O": # if it's an O remember there's an O more in the playing grid
                nCircle += 1
        i += 1

    if not(nCross == nCircle or nCross == nCircle+1): # Checks if the playing order is right by seeing if #X are as equal or just one more of #O
        return False # if not, no more checks are needed
    
    # Checks if the game has had a win and still kept going
    if count_wins(matrix)>1:
        return False
    
    return True