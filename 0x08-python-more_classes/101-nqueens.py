#!/usr/bin/python3
"""Solves the N-queens puzzle.

Example:
    $ ./101-nqueens.py N

Attributes:
    chessboard (list): lists representing the chessboard.
    solutions (list): lists containing solutions.
"""
import sys


def get_s(chessboard):
    """Return lists representation of a solved chessboard."""
    s = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                s.append([r, c])
                break

    return (s)

def init_chessboard(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    chessboard = []
    for i in range(n):
        chessboard.append([])

    [row.append(' ') for i in range(n) for row in chessboard]
    return (chessboard)


def chessboard_deepcopy(chessboard):
    """Return a deepcopy"""
    if isinstance(chessboard, list):
        return list(map(chessboard_deepcopy, chessboard))

    return (chessboard)


def xout(chessboard, row, column):
    """X out spots on a chessboard.

    Args:
        chessboard (list): current chessboard.
        row (int): The row where a queen was last played.
        column (int): The colum where a queen was last played.
    """
    for c in range(column + 1, len(chessboard)):
        chessboard[row][c] = "x"

    for c in range(column - 1, -1, -1):
        chessboard[row][c] = "x"

    for r in range(row + 1, len(chessboard)):
        chessboard[r][column] = "x"

    for r in range(row - 1, -1, -1):
        chessboard[r][column] = "x"

    c = column + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1

    c = column - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c]
        c -= 1

    c = column + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1

    c = column - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def rec_solve(chessboard, row, queens, s):
    """solve an N-queens puzzle.

    Args:
        chessboard (list): current chessboard.
        row (int): current row.
        queens (int): current place of queens.
        s (list): lists of solutions.
    Returns:
        s
    """
    if queens == len(chessboard):
        s.append(get_s(chessboard))
        return (s)

    for c in range(len(chessboard)):
        if chessboard[row][c] == " ":
            tmp_chessboard = chessboard_deepcopy(chessboard)
            tmp_chessboard[row][c] = "Q"
            xout(tmp_chessboard, row, c)
            s = rec_solve(tmp_chessboard, row + 1,
                                        queens + 1, s)

    return (s)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = init_chessboard(int(sys.argv[1]))
    solutions = rec_solve(chessboard, 0, 0, [])
    for sol in solutions:
        print(sol)
