# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_count = 1
        queue = [(root, 1)]
        """
        left of node at ith position is at  2*i and right is at 2*i+1.
        Assign postions to nodes.
        Width of a level is difference of positions between the leftmost and rightmost nodes in that level
        """
        while queue:
            nqueue = []

            while queue:
                t, val = queue.pop(0)

                if t.left:
                    nqueue.append((t.left, 2*val))
                if t.right:
                    nqueue.append((t.right, 2*val+1))
            if len(nqueue) > 1:
                max_count = max(max_count, nqueue[-1][1] - nqueue[0][1] + 1)
            if nqueue:
                queue = [x for x in nqueue]


        return max_count
