# Sudoku-Solver
It solves an entire 9x9 solvable Sudoku and returns the solved version into a neat text file for later use.

Sudoku Solver
This Python script solves Sudoku puzzles using a backtracking algorithm. It reads an unsolved Sudoku puzzle from a text file, solves it, and writes the solved puzzle to another text file.

Features
Solves 9x9 Sudoku puzzles.
Reads unsolved Sudoku puzzles from a text file.
Writes solved Sudoku puzzles to a text file.
Utilizes a backtracking algorithm to efficiently find solutions.

Requirements
Python

Usage
Place the unsolved Sudoku puzzle in a text file named sudoku_unsolved.txt.
Run the sudoku_solver.py script.
The script will solve the Sudoku puzzle and write the solved puzzle to sudoku_solved.txt.

Input Format
The unsolved Sudoku puzzle should be provided in the following format:
Use '0' or any other placeholder for empty cells.
Each row of the puzzle should be represented as a space-separated string of numbers.
The entire puzzle should be represented as 9 rows in the text file.

Example
0 0 0 2 6 0 7 0 1
6 8 0 0 7 0 0 9 0
1 9 0 0 0 4 5 0 0
8 2 0 1 0 0 0 4 0
0 0 4 6 0 2 9 0 0
0 5 0 0 0 3 0 2 8
0 0 9 3 0 0 0 7 4
0 4 0 0 5 0 0 3 6
7 0 3 0 1 8 0 0 0


Output Format
The solved Sudoku puzzle will be written to sudoku_solved.txt in the same format as the input file.

Author
Khandaker Menon Zaman Pranto
