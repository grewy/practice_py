# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []

        if not root:
            return res

        while True:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.right

            if not stack:
                break
            root = stack.pop(-1)
            root= root.left

        return res[::-1]

