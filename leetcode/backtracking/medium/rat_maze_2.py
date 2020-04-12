
N = 4

def is_safe(board, x, y):
    if x >= 0 and y >= 0 and x < N and y < N and board[x][y] == 1:
        return True
    return False

def print_sol(board):
    for i in board:
        for j in i:
            print str(j) + " ",
        print


def maze_util(maze, x, y, sol):
    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    if is_safe(maze, x, y):
        sol[x][y] = 1

        if maze_util(maze, x, y+1, sol):
            return True

        if maze_util(maze, x+1, y, sol):
            return True

        sol[x][y] = 0
        return False

def maze_sol(maze):
    sol = [[0 for _ in range(N)] for _ in range(N)]

    if maze_util(maze, 0, 0, sol):
        print_sol(sol)
    else:
        print "solution not found"




if __name__ == "__main__":
        # Initialising the maze
        maze = [[1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 1, 0, 1],
                [1, 1, 1, 1]]

        maze_sol(maze)