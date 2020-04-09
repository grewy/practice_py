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
        self.count = 0
        def runDFS(node, arr):
		    if not node:
			    return arr

		    arr = [num + node.val for num in arr] + [node.val]

		    for num in arr:
			    if num == sm:
				    self.count += 1

		    runDFS(node.left, arr)
		    runDFS(node.right, arr)

	runDFS(root, [])
	return self.count
