# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        #root is one of the node
        if root == p or root == q:
            return root

        #one node in left subtree of root and other in right subtree
        lt_lca = self.lowestCommonAncestor(root.left, p, q)
        rt_lca = self.lowestCommonAncestor(root.right, p, q)
        if lt_lca and rt_lca:
            return root

        #both nodes in left subtree of root or right subtree of root
        if lt_lca:
            return lt_lca
        else:
            return rt_lca
