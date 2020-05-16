
from collections import deque

grid = [['X', '0', '0'],
        ['X', '0', '0'],
        ['0', 'Y', 'Y']]


def bfs(grid):

    q, visited = deque(), set()
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                q.append(((i,j), (i, j)))
                visited.add((i,j))

    while q:
        (r, c), (rs, cs) = q.popleft()
        if grid[r][c] == 'Y':
            return [(rs,cs), (r,c)]

        for _dir in dirs:
            new_pos = (new_r, new_c) = r + _dir[0], c + _dir[1]
            if new_r < 0 or new_c < 0 or new_r>=len(grid) or new_c>=len(grid[0]) or new_pos in visited:
                continue
            q.append(((new_r, new_c), (rs,cs)))
            visited.add(new_pos)

    return -1

print(bfs(grid))
