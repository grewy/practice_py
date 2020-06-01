# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1

        def depth(root):
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            self.ans = max(self.ans, l + r +1)
            return max(l, r) + 1

        depth(root)
        return self.ans - 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.ans = float('-inf')

        def height(root):
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)

            # Diameter of tree is maximum value of (lheight + rheight +1 ) for each node
            self.ans = max(self.ans, lh + rh + 1)
            return 1 + max(lh, rh)


        height(root)
        return self.ans - 1


