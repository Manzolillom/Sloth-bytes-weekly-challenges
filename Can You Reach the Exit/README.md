 You are given a 2D grid where each cell is one of:

    '.' - empty space (you can walk here)

    '#' - wall (you cannot walk here)

    '@' - starting position

    'E' - exit 

You can move up, down, left, right (no diagonals), and you cannot move outside the grid. 

### Examples:
```
can_reach_exit([
    "@..",
    ".#E",
    "..."
])
output = True
# One path: (0,0)->(0,1)->(0,2)->(1,2) which is 'E'

can_reach_exit([
    "@#E"
])
output = False
# Exit is blocked by a wall

can_reach_exit([
    "@.#.",
    "..#E",
    "####"
])
output = False

can_reach_exit([
    "@...",
    ".###",
    "...E"
])
output = True
```
### Notes:
Find the exit recursively, at each intersection start a new function for each path:
The straight line to win is the default case, if it's blocked false, otherwise true

December 02, 2025 
https://slothbytes.beehiiv.com/p/being-wrong-is-your-job