# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sm):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            stack = [(root,0)]
            while stack:
                curr_node,path_sum = stack.pop()

                path_sum += curr_node.val

                if(not curr_node.left and not curr_node.right):
                    if path_sum==sm:
                        return True
                else:
                    if curr_node.left:
                        stack.append((curr_node.left,path_sum))

                    if curr_node.right:
                        stack.append((curr_node.right,path_sum))

        return False
