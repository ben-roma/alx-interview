# 0x05-nqueens

This project tackles the classic N-queens problem, a puzzle that involves placing N chess queens on an N×N chessboard so that no two queens threaten each other. In other words, no two queens can share the same row, column, or diagonal.

## Learning Objectives

By completing this project, you will:

* Gain a deeper understanding of backtracking algorithms and their applications.
* Learn how to implement recursive solutions to complex problems.
* Improve your problem-solving skills in the context of algorithmic challenges.
* Practice manipulating lists and other data structures in Python.
* Handle command-line arguments effectively in Python scripts.

## Project Structure

The project contains the following file:

* **0-nqueens.py:** A Python script that solves the N-queens problem for a given board size N.

## Task

### 0. N queens

* Write a program that solves the N queens problem.
    * Usage: `nqueens N`
    * Where N must be an integer greater or equal to 4
    * If the user calls the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
    * If
    * If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status `1`
    * The program should print every possible solution to the problem
        * One solution per line
        * You don’t have to print the solutions in a specific order
    * You are only allowed to import the `sys` module

## Technologies Used

* Python

## Resources

* [Queen](https://en.wikipedia.org/wiki/Queen_(chess))
* [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
