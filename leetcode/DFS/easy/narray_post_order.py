"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def _postorder(node):
            if node:
                for child in node.children:
                    _postorder(child)
                res.append(node.val)

        res = []
        _postorder(root)
        return res

