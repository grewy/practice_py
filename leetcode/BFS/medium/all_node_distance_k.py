# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        parents = {}

        def get_parents(root, parent):
            if root is None:
                return

            parents[root.val] = parent
            get_parents(root.left, root)
            get_parents(root.right, root)


        def bfs(start, k):
            res = []
            q = [(start, 0)]
            visited = set()

            while q:
                c, d = q.pop(0)

                if c not in visited:
                    visited.add(c)
                    if d == k:
                        res.append(c.val)

                    if c.left:
                        q.append((c.left, d+1))

                    if c.right:
                        q.append((c.right, d+1))

                    if parents[c.val]:
                        q.append((parents[c.val], d+1))

            return res

        get_parents(root, None)
        print "here"
        return bfs(target, K)






