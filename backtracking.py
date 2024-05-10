# import copy

# def validate_board( board , row , X_i ):
#     for i in range(row):
#         if board[i] == X_i or abs( board[i] - X_i ) == abs( i - row ):
#             return False
#     return True

# def print_board( board ):
#     print( board )
#     print( "==" * 6 )

# def solve_n_queens( board ):
#     global N
#     print_board( board )
#     i = 0
#     while i < N and board[i] != -1:
#         i += 1
#     if i == N:
#         print_board( board )
#         print( "Solved!" ) 
#         return True
#     for X_i in range( N ):
#         if validate_board(board, i, X_i):
#             child_board = copy.deepcopy( board )
#             child_board[i] = X_i
#             if solve_n_queens(child_board):
#                 return True
#     return False

# N = 4
# board = [ -1 for _ in range(N) ]
# print_board(board)
# print( solve_n_queens(board) )

def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_nqueens_backtracking(board, col, n):
    # If all queens are placed, return True
    if col >= n:
        return True

    # Try placing the queen in each row one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place the queen
            board[i][col] = 'Q'

            # Recur to place the rest of the queens
            if solve_nqueens_backtracking(board, col + 1, n):
                return True

            # If placing the queen doesn't lead to a solution, backtrack
            board[i][col] = '.'

    return False


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def solve_nqueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]

    if solve_nqueens_backtracking(board, 0, n):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists")


# Test the backtracking solution
solve_nqueens(8)  # 8-queens problem
