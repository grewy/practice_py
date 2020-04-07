class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return

        stack = [root]
        result = [[root]]
        while stack:
            nstack = []
            while stack:
                el = stack.pop(0)

                if el.left:
                    nstack.append(el.left)
                if el.right:
                    nstack.append(el.right)
            if nstack:
                result.append([x for x in nstack])
            stack=nstack

        for x in result:
            for k, v in enumerate(x[:-1]):
                v.next = x[k+1]
        return root
