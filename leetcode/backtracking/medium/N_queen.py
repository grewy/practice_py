
N = 4

def print_sol(board):
    for i in range(N):
        for j in range(N):
            print board[i][j],
        print


def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1):
                return True
        board[i][col] = 0
    return False


##########
def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    if solveNQUtil(board, 0):
        print_sol(board)
    else:
        print "solution not found"


# Driver Code
solveNQ()