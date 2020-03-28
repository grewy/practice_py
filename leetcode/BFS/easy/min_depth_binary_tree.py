class Solution(object):
    def minDepth(self, root, level=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = [root]
        depth = 0
        while stack:
            depth += 1
            newstack = []
            while stack:
                node = stack.pop()

                if not any([node.left, node.right]):
                    return depth

                if node.left:
                    newstack.append(node.left)
                if node.right:
                    newstack.append(node.right)

            stack = newstack
        return depth
