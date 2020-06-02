def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        """
        while True:
            while root:
                stack.append(root)
                root = root.left
            # pop left most
            root = stack.pop(-1)

            k -= 1
            if not k:
                return root.val
            root=root.right
        """
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur =cur.left
            else:
                cur = stack.pop()
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right

        return -1
