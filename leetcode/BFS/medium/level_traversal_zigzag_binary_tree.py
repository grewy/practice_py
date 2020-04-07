class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ltor = 1
        stack = [root]
        res = [[root.val]]

        while stack:

            nstack = []
            ltor = ltor ^ 1
            while stack:
                n = stack.pop(0)

                if n.left:
                    nstack.append(n.left)
                if n.right:
                    nstack.append(n.right)

            if nstack:
                a = [x.val for x in nstack]
                if not ltor:
                    a = a[::-1]
                res.append(a)
            stack = nstack
        return res
