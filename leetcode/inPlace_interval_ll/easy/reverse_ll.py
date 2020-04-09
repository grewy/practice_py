# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        p = head
        tmp = p.next
        p.next = None

        while tmp:
            q = tmp.next
            tmp.next = p
            p = tmp
            tmp = q

        return p

