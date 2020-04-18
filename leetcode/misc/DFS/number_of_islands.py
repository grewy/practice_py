def count_islands():
    visited = [[False for j in range(N)] for i in range(M)]

    count = 0
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and graph[i][j] == 1:
                DFS(i, j, visited)
                count += 1

    return count

def DFS(i, j, visited):
    row_nbr = [-1, -1, -1,  0, 0,  1, 1, 1]
    col_nbr = [-1,  0,  1, -1, 1, -1, 0, 1]

    visited[i][j] = True

    for k in range(len(row_nbr)):
        if is_safe(i+row_nbr[k], j+col_nbr[k], visited):
            DFS(i+row_nbr[k], j+col_nbr[k], visited)

def is_safe(i, j, visited):
    return (i>=0 and i<M) and (j>=0 and j<N) and not visited[i][j] and graph[i][j]


graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1]]

M = len(graph)
N = len(graph[0])

print count_islands()
