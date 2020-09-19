# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, prev_val):
            if node is None:
                return 0

            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)

            self.max_val = max(self.max_val, left+right)

            return max(left, right) + 1 if node.val == prev_val else 0

        if root is None:
            return 0
        self.max_val = 0
        dfs(root, root.val)
        return self.max_val

