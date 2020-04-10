# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            h = head.next
            if h:
                h.next, head.next = head, h.next
                h.next.next = self.swapPairs(h.next.next)
                return h
        return head
