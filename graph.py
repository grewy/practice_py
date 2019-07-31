# Python program to print DFS traversal from a
# given given graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:

  # Constructor
  def __init__(self):

    # default dictionary to store graph
    self.graph = defaultdict(list)

  # function to add an edge to graph
  def addEdge(self, u, v):
    self.graph[u].append(v)

  # A function used by DFS
  def DFSUtil(self, v, visited):

    # Mark the current node as visited and print it
    visited[v] = True
    print v,

    # Recur for all the vertices adjacent to this vertex
    for i in self.graph[v]:
      if visited[i] == False:
        self.DFSUtil(i, visited)

  # The function to do DFS traversal. It uses
  # recursive DFSUtil()
  def DFS(self, v=None):

    # Mark all the vertices as not visited
    visited = [False] * (len(self.graph))

    # Call the recursive helper function to print
    # DFS traversal
    if v is not None:
      self.DFSUtil(v, visited)
    else:
      for i in range(len(self.graph)):
        print i, ": ",
        self.DFSUtil(i, visited)
        print

  # Function to print a BFS of graph
  def BFS(self, s):
    visited = [False] * (len(self.graph))

    queue = []

    queue.append(s)
    visited[s] = True

    while queue:

      s = queue.pop(0)
      print s,

      for i in self.graph[s]:
        if visited[i] == False:
          queue.append(i)
          visited[i] = True

  def shortestPath(self, s):
    q = [s]
    visited = set()
    visited.add(s)
    parent = {s:None}
    distance = {s:0}
    while len(q) > 0:
      cur = q.pop(0)
      for dest in self.graph[cur]:
        if dest not in visited:
          visited.add(dest)
          parent[dest] = cur
          distance[dest] = distance[cur] + 1
          q.append(dest)
    return (parent, distance)
# Driver code
# Create a graph given in the above diagram
# 0-----1
#  \\   |
#   \\  |
#    \\ |
#      2------3<=>

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
#g.addEdge(3,4)
#g.addEdge(4,1)

print g.DFS(1)