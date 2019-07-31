from collections import deque

import copy

from stack import Stack

class TreeNode(object):

  def __init__(self, data, left_child=None, right_child=None):
    self.data = data
    self.left_child = left_child
    self.right_child = right_child


class BTree(object):


  def __init__(self, root):
    self.root = root

  def inorder(self, root):
    if not root:
      return
    else:
      if root.left_child:
        self.inorder(root.left_child)
      print root.data,
      if root.right_child:
        self.inorder(root.right_child)

  def preorder(self, root):
    if not root:
      return
    else:
      print root.data,
      if root.left_child:
        self.inorder(root.left_child)
      if root.right_child:
        self.inorder(root.right_child)

  def postorder(self, root):
    if not root:
      return
    else:
      if root.left_child:
        self.inorder(root.left_child)
      if root.right_child:
        self.inorder(root.right_child)
      print root.data,

  def height(self, root):
    if not root:
      return 0
    else:
      return max(self.height(root.left_child),
                 self.height(root.right_child)) + 1

  def getMax(self, root, mx=0):
    if root is None:
      return mx
    else:
      if mx < root.data:
        mx=root.data

      return max(self.getMax(root.left_child, mx=mx),
                 self.getMax(root.right_child,mx=mx))

  def level(self, root):
    if root is None:
      return
    q = deque()
    q.append(root)
    while len(q) > 0:
      tmp = q.popleft()
      print tmp.data,
      if tmp.left_child is not None:
        q.append(tmp.left_child)
      if tmp.right_child is not None:
        q.append(tmp.right_child)

  def max_level(self, root):
    if root is not None:
      q= deque()
      mx = 0
      q.append(root)
      while len(q) > 0:
        tmp = q.popleft()
        if mx < tmp.data:
          mx = tmp.data
        if tmp.left_child is not None:
          q.append(tmp.left_child)
        if tmp.right_child is not None:
          q.append(tmp.right_child)
      return mx

  def reverse_level(self, root):
    if root is None:
      return
    q = deque()

    q.append(root)
    s = Stack()
    s.push(root.data)
    while len(q) > 0:
      tmp = q.popleft()
      if tmp.left_child is not None:
        q.append(tmp.left_child)
        s.push(tmp.left_child.data)

      if tmp.right_child is not None:
        q.append(tmp.right_child)
        s.push(tmp.right_child.data)

    while not s.isEmpty():
      print s.pop(),

  def delete_tree(self, root):
    if root is None:
      return
    self.delete_tree(root.left_child)
    self.delete_tree(root.right_child)
    root.left_child = None
    root.right_child = None
    root.data = None

  def printLeafpath(self, root):
    if root is None:
      return []
    if (root.left_child == None and root.right_child == None):
      return [str(root.data)]

      # subtree is always a list, though it might be empty
    left_subtree = self.printLeafpath(root.left_child)
    right_subtree = self.printLeafpath(root.right_child)
    full_subtree = left_subtree + right_subtree  # the last part of comprehension

    list1 = []
    for leaf in full_subtree:  # middle part of the comprehension
      list1.append(str(root.data) + '->' + leaf)  # the left part

    return list1

  def check_sum(self, root, sm):
    if root is None:
      return sm == 0
    else:
      resm = sm - root.data
      return self.check_sum(root.left_child, resm) or \
             self.check_sum(root.right_child, resm)

  def side_view(self, root, LEFTVIEW=True):
    if root is None:
      return

    q = deque()
    q.append(root)

    while len(q) > 0:
      count = len(q)
      level_flag = True
      while count > 0:
        t = q.popleft()
        count = count - 1
        if level_flag and LEFTVIEW:
            print t.data,
            level_flag = not level_flag
        if not LEFTVIEW and count==0:
          print t.data,
          level_flag = not level_flag
        if t.left_child is not None:
          q.append(t.left_child)
        if t.right_child is not None:
          q.append(t.right_child)

  def is_BST(self, root, l=None, r=None):

    if root is None:
      return True

    if l is not None and root.data < l.data:
      return False

    if r is not None and root.data > r.data:
      return False

    return self.is_BST(root.left_child, l, root) and \
           self.is_BST(root.right_child, root, r)



####################################################################
# Using the binary tree
a = TreeNode(4, None, None)
b = TreeNode(2, None, None)
c = TreeNode(7, None, None)
d = TreeNode(1, None, None)
e = TreeNode(3, None, None)
f = TreeNode(6, None, None)
g = TreeNode(8, None, None)
h = TreeNode(5, None, None)

a.left_child, a.right_child = b, c
b.left_child, b.right_child = d, e
c.left_child, c.right_child = f, g
f.left_child = h

'''
         1a
      /     \
     2 b     5 c
    / \    / \
   d3 4e  f6  g7  
         /
        8h 
'''


btree = BTree(a)

if btree.is_BST(btree.root):
  print "It's a BST"
else:
  print "not a BST"


