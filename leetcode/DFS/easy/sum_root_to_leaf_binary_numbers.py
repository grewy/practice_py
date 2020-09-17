# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leaf_path = 0
        stack = [(root, 0)]

        while stack:
            root, cur_num = stack.pop()
            if root is not None:
                cur_num = (cur_num << 1) | root.val
                if root.left is None and root.right is None:
                    leaf_path += cur_num
                else:
                    stack.append((root.left, cur_num))
                    stack.append((root.right, cur_num))

        return leaf_path

