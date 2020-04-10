# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        odd_head = None
        even_head = None

        t = head
        tmp = head
        while t:
            if t.val % 2 == 0:
                if not even_head:
                    even_head = t
                    tmp = even_head
                else:
                    even_head.next = t
                    even_head = even_head.next
            else:
                if not odd_head:
                    odd_head = t
                    head = odd_head
                else:
                    odd_head.next = t
                    odd_head = odd_head.next
            t = t.next

        odd_head.next = tmp
        return head
