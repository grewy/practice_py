class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_val = p.val
        q_val = q.val
        node = root

        while node:
            parent_val = node.val
            if p_val > parent_val and q_val> parent_val:
                node = node.right
            elif p_val <parent_val and q_val < parent_val:
                node = node.left
            else:
                return node
