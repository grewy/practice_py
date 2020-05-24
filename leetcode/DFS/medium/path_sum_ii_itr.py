"""
DFS + stack
113. Path Sum II
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sm):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return []
        stack = [(root, [root.val])]
        while stack:
            cur, cur_path = stack.pop()
            if not cur.left and not cur.right and sum(cur_path) == sm:
                ans.append(cur_path)
            if cur.right:
                stack.append((cur.right, cur_path + [cur.right.val]))
            if cur.left:
                stack.append((cur.left, cur_path + [cur.left.val]))
        return ans

