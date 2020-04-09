# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        q = deque()
        q.append(root)
        while q:
            curr = q.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root


