# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        stack = [root]
        prev = 0
        while stack:
            nstack = []
            _next = 0
            while stack:
                root = stack.pop()
                if root.left:
                    nstack.append(root.left)
                    _next += root.left.val
                if root.right:
                    nstack.append(root.right)
                    _next += root.right.val

            stack = nstack
            if _next > 0:
                prev = _next
        return prev
