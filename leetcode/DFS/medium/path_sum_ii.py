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
        :rtype: List[List[int]]
        """
        solution = []
        current_path = []

        def helper( node):
            if not node:
                return

            current_path.append( node.val )

            if not node.left and not node.right and sum(current_path) == sm:
                solution.append( list(current_path) )

            helper( node.left )
            helper( node.right )

            current_path.pop()

        helper(root)
        return solution
