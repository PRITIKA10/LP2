def solve_nqueens_branch_and_bound(col, n, rows, diag1, diag2, board):
    # If all queens are placed, return True
    if col >= n:
        return True

    for row in range(n):
        if row in rows or (col - row) in diag1 or (col + row) in diag2:
            # This row/diagonal is under attack
            continue
        
        # Place the queen
        board[row][col] = 'Q'
        rows.add(row)
        diag1.add(col - row)
        diag2.add(col + row)

        if solve_nqueens_branch_and_bound(col + 1, n, rows, diag1, diag2, board):
            return True
        
        # Backtrack if placing doesn't lead to a solution
        board[row][col] = '.'
        rows.remove(row)
        diag1.remove(col - row)
        diag2.remove(col + row)

    return False


def solve_nqueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    rows = set()  # Set of rows under attack
    diag1 = set()  # Set of main diagonals under attack
    diag2 = set()  # Set of anti-diagonals under attack

    if solve_nqueens_branch_and_bound(0, n, rows, diag1, diag2, board):
        print("Solution found:")
        for row in board:
            print(" ".join(row))
        print()
    else:
        print("No solution exists")


# Test the branch and bound solution
solve_nqueens(8)  # 8-queens problem
