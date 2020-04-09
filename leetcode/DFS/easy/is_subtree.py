# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isId(root, p):
            if not root and not p:
                return True
            if not root or not p:
                return False

            return root.val == p.val and isId(root.left, p.left) and isId(root.right, p.right)

        def traverse(s, t):
            return s and (isId(s,t) or traverse(s.left, t) or traverse(s.right, t))

        return traverse(s, t)




