# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if not root:
            return []

        to_del = set(to_delete)
        roots = {root}

        def helper(node):
            if not node:
                return False

            if helper(node.left):
                node.left = None
            if helper(node.right):
                node.right = None

            if node.val in to_del:
                if node.left:
                    roots.add(node.left)
                if node.right:
                    roots.add(node.right)
                return True
            return False

        if helper(root):
            roots.remove(root)
        return roots

