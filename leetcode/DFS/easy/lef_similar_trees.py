# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaves(node, leaves):
            if node:
                if node.left or node.right:
                    get_leaves(node.left, leaves)
                    get_leaves(node.right, leaves)
                else:
                    leaves.append(node.val)
            return leaves

        return get_leaves(root1, []) == get_leaves(root2, [])


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        stack = [root1]
        leaves = []
        while stack:
            cur = stack.pop(0)
            if not cur.left and not cur.right:
                leaves.append(cur.val)
            if cur.right:
                stack.insert(0, cur.right)
            if cur.left:
                stack.insert(0, cur.left)

        stack = [root2]

        while stack and leaves:
            cur = stack.pop(0)
            if not cur.left and not cur.right:
                if cur.val != leaves[0]:
                    return False
                else:
                    leaves.pop(0)
            if cur.right:
                stack.insert(0, cur.right)
            if cur.left:
                stack.insert(0, cur.left)

        if len(leaves) > 0 or len(stack) > 0:
            return False
        return True
