import sys

def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(N, 0, board)

def solve_nqueens(N, row, board):
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row+1, board)
            board[row] = -1

def is_safe(board, row, col):
    for i in range(row):
        if (board[i] == col or
        board[i] - i == col - row or
        board[i] + i == col + row):
            return False
        return True

def print_solution(board):
    N = len(board)
    for row in range(N):
        line = ""
        for col in range(N):
            if board[row] == col:
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
            nqueens(N)

        except ValueError:
            print("N must be a number")
            sys.exit(1)
