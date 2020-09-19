"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def _preorder(node):
            if node:
                res.append(node.val)
                for child in node.children:
                    _preorder(child)

        res = []
        _preorder(root)
        return res
