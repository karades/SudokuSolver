# SudokuSolver
Sudoku Solver in Python

I wanted to use here not only recursion to solve our sudoku, but firstly try to solve it with basic methods, then if it is needed, use recursion to solve it.

At the beginning, it checks by square possible values, which are hold in 3d list. If there is one possiibility of number for cell or there is one number in cell, which can't be put elsewhere, it puts it on board cell.

Then it does the same for horizontal and vertical lines.

At the end, if there are 2 iterations, which gives us no difference in possibility board or main board, it uses recursion to put possible value at the empty board cell, then try to solve it. If it is impossible, it tries another one until it is solved.
