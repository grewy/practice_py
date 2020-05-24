# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        root = TreeNode(max(nums))
        stack = [(root, nums)]
        while stack:
            c, ls = stack.pop()
            idx = ls.index(c.val)
            if ls[idx+1:]:
                c.right = TreeNode(max(ls[idx+1:]))
                stack.append((c.right, ls[idx+1:]))
            if ls[:idx]:
                c.left = TreeNode(max(ls[:idx]))
                stack.append((c.left, ls[:idx]))
        return root

