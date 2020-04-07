# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack = [root]
        result = [root.val]

        while stack:
            nstack = []
            while stack:
                el = stack.pop(0)
                if el.left:
                    nstack.append(el.left)
                if el.right:
                    nstack.append(el.right)
            if nstack:
                result.append(nstack[-1].val)
            stack=nstack

        return result

