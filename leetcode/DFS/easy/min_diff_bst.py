# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        cur = root
        res = float('inf')
        prev = None

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if prev is None:
                    prev = cur.val
                else:
                    if res > (cur.val - prev):
                        res = cur.val - prev
                    prev = cur.val
                cur = cur.right

        return res




