


def topo_util(graph, v, visited, stack):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            topo_util(graph, i, visited, stack)

    stack.append(v)



def topological_sort(graph, v_count):
    visited = [False]*v_count
    stack = []

    for i in range(v_count):
        if not visited[i]:
            topo_util(graph, i, visited, stack)

    return stack[::-1]


graph = [[], [], [3], [1], [0,1], [0,2]]
v_count = 6
print topological_sort(graph, v_count)
