"""
437. Path Sum III

Keep track of all path sums ending on the node and add path sum starting at the node.
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
        :rtype: int
        """
        if not root:
            return 0
        count = 0
        stack = [(root, [root.val])]
        while stack:
            cur, cur_ls = stack.pop()
            for num in cur_ls:
                if num == sm:
                    count += 1
            if cur.right:
                stack.append((cur.right, [x + cur.right.val for x in cur_ls] + [cur.right.val]))
            if cur.left:
                stack.append((cur.left, [x+cur.left.val for x in cur_ls] + [cur.left.val]))
