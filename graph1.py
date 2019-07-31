from collections import defaultdict
from stack import Stack

class Graph:

  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def DFS(self,s):
    st = Stack()
    visited = [False]*len(self.graph)
    st.push(s)
    visited[s] = True
    while not st.isEmpty():
      x = st.pop()
      print x,
      visited[x] = True
      for i in self.graph[x]:
        if not visited[i]:
          st.push(i)

  def BFS(self,s):
    q = []
    visited = [False] * len(self.graph)
    q.append(s)
    visited[s] = True
    while len(q) > 0:
      x = q.pop(0)
      print x,
      visited[x] = True
      for i in self.graph[x]:
        if not visited[i]:
          q.append(i)


############################################
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

g.BFS(1)




