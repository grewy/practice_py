"""
Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        p= root
        while root:
            cur = tmp = Node(0)
            #check current level
            while root:
                if root.left:
                    #tmp next linked to root.left
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            #move to next level
            root = tmp.next
        return p

