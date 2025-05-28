def n_queens(n):
    board = [[0] * n for  _ in range(n)]
    solve_n_queens(board,0,n)

def solve_n_queens(board,row,n):
    if row == n:
        print_board(board)
        return
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col] = 1
            solve_n_queens(board,row+1,n)
            board[row][col] = 0
def is_safe(board,row,col,n):
    for i in range(row):
        if board[i][col]:
            return False
    i , j = row , col
    while i >=0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i , j = row , col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    return True
def print_board(board):
    for row in board:
        print(" ".join('Q' if cell else '.' for cell in row))
    print()

n_queens(6)
