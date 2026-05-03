Given a board as a list of 3 strings, where each string is a row and each row contains exactly 3 characters ("X", "O", or " "). Write a function that determines whether that board state can be reached by following the rules of Tic-Tac-Toe.
Rules of Tic-Tac-Toe

    X always goes first. O goes second.

    Players take turns placing one mark at a time

    A player wins by getting 3 in a row:

        horizontally

        vertically

        diagonally

    Once someone wins, the game ends immediately

```
validateTicTacToe(["X  ", "   ", "   "])
output = true
# X always goes first, so one X is valid.

validateTicTacToe(["O  ", "   ", "   "])
output = false
# O cannot make the first move.

validateTicTacToe(["X X", " O ", "   "])
output = true
# X played twice, O once.
# This follows alternating turns = vaild.

validateTicTacToe(["XOX", " X ", "   "])
# output = false
# X has 3 moves while O has 1.
# Players must alternate, so move counts are invalid.

validateTicTacToe(["XXX", "OO ", "   "])
output = true
# X has 3 moves, O has 2.
# X completes a row on its turn, so the game can end here.

validateTicTacToe(["XXX", "   ", "OOO"])
output = false
# Both players cannot win in the same valid game.
# The game would stop as soon as the first win happens.
```

April 21, 2026
https://slothbytes.beehiiv.com/p/programming-feels-different