# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if not root:
            return res

        stack = [(root, False)]
        while stack:
            cur, is_left = stack.pop()

            if is_left and not cur.left and not cur.right:
                res += cur.val

            if cur.left:
                stack.append((cur.left, True))
            if cur.right:
                stack.append((cur.right, False))

        return res
