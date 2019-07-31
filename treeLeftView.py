


class Node:
  def __init__(self, val):
    self.right = None
    self.data = val
    self.left = None


class Tree:
  def createNode(self, data):
    return Node(data)

  def insert(self, node, data, ch):
    if node is None:
      return self.createNode(data)
    if (ch == 'L'):
      node.left = self.insert(node.left, data, ch)
      return node.left
    else:
      node.right = self.insert(node.right, data, ch)
      return node.right

  def search(self, lis, data):
    # if root is None or root is the search data.
    for i in lis:
      if i.data == data:
        return i

def printLeftView(root):
  # Code here


# Driver Program
if __name__ == '__main__':
  t = 1
  for i in range(t):
    n = 5
    arr = [1, 2, 'L', 1, 3, 'R', 2, 4, 'L', 2, 5, 'R', 5, 6, 'L']
    if n == 0:
      print('')
      continue
    tree = Tree()
    lis = []
    root = None
    root = tree.insert(root, int(arr[0]), 'L')
    lis.append(root)
    k = 0
    for j in range(n):
      ptr = None
      ptr = tree.search(lis, int(arr[k]))
      lis.append(tree.insert(ptr, int(arr[k + 1]), arr[k + 2]))
      k += 3
    printLeftView(root)
    print('')




''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the left view of the binary tree
# Note: You aren't required to print a new line after every test case


