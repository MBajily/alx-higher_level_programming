#!/usr/bin/python3

import sys

class NQueensSolver:
    def __init__(self, N):
        self.N = N
        self.board = [-1] * N

    def solve(self):
        self._solve_nqueens(0)

    def _solve_nqueens(self, row):
        if row == self.N:
            self._print_solution()
            return
        for col in range(self.N):
            if self._is_safe(row, col):
                self.board[row] = col
                self._solve_nqueens(row + 1)
                self.board[row] = -1

    def _is_safe(self, row, col):
        for i in range(row):
            if (self.board[i] == col or
                    self.board[i] - i == col - row or
                    self.board[i] + i == col + row):
                return False
            return True

    def _print_solution(self):
        for row in range(self.N):
            line = ""
            for col in range(self.N):
                if self.board[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        
        solver = NQueensSolver(N)
        solver.solve()

    except ValueError:
        print("N must be a number")
        sys.exit(1)
