Create a function that takes a 5x5 2D list and returns True if it has at least one Bingo, and False If it doesn't.

### Examples:
```
bingo_check([
  [45, "x", 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, 39, 44],
  [21, "x", 24, 30, 52]
])
output = True

bingo_check([
  ["x", 43, 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, 65, "x", 83, 54],
  [67, 98, 39, "x", 44],
  [21, 59, 24, 30, "x"]
]) 
output = True

bingo_check([
  ["x", "x", "x", "x", "x"],
  [64, 12, 47, 32, 90],
  [37, 16, 68, 83, 54],
  [67, 19, 98, 39, 44],
  [21, 75, 24, 30, 52]
]) 
output = True

bingo_check([
  [45, "x", 31, 74, 87],
  [64, 78, 47, "x", 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, "x", 44],
  [21, "x", 24, 30, 52]
]) 
output = False
```
### Notes:

you just need to check the diagonal: (<- I used this one)
- for each string in the diagonal: 
    - if it's an x, check column and row 
        - if it's a bingo in column or row return true
    - keep a bool variable (instantiated at true) till the end , if you find something different than a x in the diagonal: make it false; return it at the end of the program (if it didn't return already from row/column bingos)
    - ISSUE: How to do for the other diagonal possible?

Another approach could be to check it like it's a factorial, if it makes sense, first the first row and column, then the second row and column, then the third, fourth and fifth. at the end the 2 diagonals.

January 27, 2026 
https://slothbytes.beehiiv.com/p/managing-data-is-complicated