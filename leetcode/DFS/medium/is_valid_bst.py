# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def valid(self, root, lower, upper):
        if not root:
            return True

        if lower is not None and lower >= root.val:
            return False
        if upper is not None and upper <= root.val:
            return False

        return self.valid(root.left, lower, root.val) and self.valid(root.right, root.val, upper)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, None, None)

