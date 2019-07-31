from tree import BTree, TreeNode





#### driver
a = TreeNode(1, None, None)
b = TreeNode(2, None, None)
c = TreeNode(5, None, None)
d = TreeNode(3, None, None)
e = TreeNode(4, None, None)
f = TreeNode(6, None, None)
g = TreeNode(7, None, None)
h = TreeNode(8, None, None)

a.left_child, a.right_child = b, c
b.left_child, b.right_child = d, e
c.left_child, c.right_child = f, g
f.left_child = h

'''
         1
      /     \
     2      5
    / \    / \
   3  4   6  7  
         /
        8 
'''


btree = BTree(a)