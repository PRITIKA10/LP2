import copy

def validate_board( board , row , X_i ):
    for i in range(row):
        if board[i] == X_i or abs( board[i] - X_i ) == abs( i - row ):
            return False
    return True

def print_board( board ):
    print( board )
    print( "==" * 6 )

def solve_n_queens( board ):
    global N
    print_board( board )
    i = 0
    while i < N and board[i] != -1:
        i += 1
    if i == N:
        print_board( board )
        print( "Solved!" ) 
        return True
    for X_i in range( N ):
        if validate_board(board, i, X_i):
            child_board = copy.deepcopy( board )
            child_board[i] = X_i
            if solve_n_queens(child_board):
                return True
    return False

N = 4
board = [ -1 for _ in range(N) ]
print_board(board)
print( solve_n_queens(board) )