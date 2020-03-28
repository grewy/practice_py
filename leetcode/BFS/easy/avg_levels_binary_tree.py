class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def avg(a):
            if len(a) < 1:
                return 0
            a = [x.val for x in a]
            return sum(a)/float(len(a))

        if not root:
            return 0

        stack = [root]
        depth = [root.val]
        while stack:

            nstack = []

            while stack:
                n = stack.pop()

                if n.left:
                    nstack.append(n.left)
                if n.right:
                    nstack.append(n.right)

            if nstack:
                depth.append(avg(nstack))
            stack = nstack
        return depth
