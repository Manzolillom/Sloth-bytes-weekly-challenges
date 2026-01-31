#   '.' - empty space (you can walk here)
#   '#' - wall (you cannot walk here) ALSO path already walked on
#   '@' - starting position
#   'E' - exit 

mappa : list[list[str]]

class ExitFoundException(Exception):
    pass

def find_start_position() -> list[int]:
    for row in range(len(mappa)):
        for column in range(len(mappa[row])):
            if mappa[row][column] == "@":
                return [row, column]
    raise Exception("no starting point found")


def is_in_boundary(row:int, column:int) -> bool:
    if row < 0 or row >= len(mappa):
        return False
    if column < 0 or column >= len(mappa[row]):
        return False
    return True

def try_to_walk_on(row:int, column:int) -> bool:
    if not is_in_boundary(row,column):
        return False
    if mappa[row][column] == 'E':
        raise ExitFoundException
    if mappa[row][column] == '.':
        mappa[row][column] = '#'
        return True
    
    return False

def possible_directions(position: list[int]) -> list[list[int]]:
    row, column = position
    possible_paths = []
    
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0)   # up
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = column + dc
        if try_to_walk_on(new_row, new_col):
            possible_paths.append([new_row, new_col])

    return possible_paths


def spread(position : list[int]):
    row, col = position
    if mappa[row][col] == 'E':
        raise ExitFoundException
    
    for path in possible_directions(position):
        spread(path)

# Substitutes all . with # if already stepped on. spread like a parasite until it finds the end or finishes possible routes
def can_reach_exit(map: list[str]) -> bool:
    global mappa
    mappa = [list(riga) for riga in map]
    position = find_start_position()
    mappa[position[0]][position[1]] = '#'
    try:
        spread(position)
    except ExitFoundException:
        return True
    return False