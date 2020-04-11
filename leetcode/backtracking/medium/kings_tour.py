

n = 8


def is_safe(x, y, board):
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False

def print_solution(board):
    '''
        A utility function to print Chessboard matrix
    '''
    for i in range(n):
        for j in range(n):
            print board[i][j],
        print

def solve_KT():
    #initialize board to -1, none visited
    board = [[-1 for i in range(n)]for i in range(n)]

    #possible x, y next moves
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    #Knight's initial position
    board[0][0] = 0
    #position counter
    pos = 1

    #print if solution found
    if solveKTUtil(board, 0, 0, x_move, y_move, pos):
        print_solution(board)
    else:
        print "solution not found"

def solveKTUtil(board, curr_x,curr_y, x_move, y_move,pos):
    #print "in solve KTU, pos: %s" % pos
    #visited all positions
    if pos == n**2:
        return True

    #try all possible moves from current position
    for i in range(n):
        new_x = curr_x + x_move[i]
        new_y = curr_y + y_move[i]

        # check if new positon is safe
        if is_safe(new_x,new_y,board):
            board[new_x][new_y] = pos
            #check next moves from current position
            if solveKTUtil(board,new_x,new_y,x_move,y_move,pos+1):
                return True

            #BackTrack if solution not found in above steps
            board[new_x][new_y] = -1
    return False


#if __name__ == "__main__":
solve_KT()
