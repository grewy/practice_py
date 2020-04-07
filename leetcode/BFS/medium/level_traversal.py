class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack = [root]
        res = [[root.val]]

        while stack:

            nstack = []

            while stack:
                n = stack.pop(0)

                if n.left:
                    nstack.append(n.left)
                if n.right:
                    nstack.append(n.right)

            if nstack:
                res.append([x.val for x in nstack])
            stack = nstack
        return res
