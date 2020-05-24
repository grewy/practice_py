# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
#     def valid(self, root, lower, upper):
#         if not root:
#             return True

#         if lower is not None and lower >= root.val:
#             return False
#         if upper is not None and upper <= root.val:
#             return False

#         return self.valid(root.left, lower, root.val) and self.valid(root.right, root.val, upper)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # return self.valid(root, None, None)

        stack = []
        pre=None
        if not root:
            return True

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            root = stack.pop(-1)
            if pre and root.val <= pre.val:
                return False

            pre = root
            root= root.right

        return True


