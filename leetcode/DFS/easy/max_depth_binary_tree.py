# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_depth = 0
        if root:
            stack = [(root,0)]
            while stack:
                curr_node, path_sum = stack.pop()

                path_sum += 1

                if(not curr_node.left and not curr_node.right):
                    max_depth = max(max_depth, path_sum)
                else:
                    if curr_node.left:
                        stack.append((curr_node.left,path_sum))

                    if curr_node.right:
                        stack.append((curr_node.right,path_sum))

        return max_depth

