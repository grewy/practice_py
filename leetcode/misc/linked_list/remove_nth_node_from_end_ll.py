# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n==0 or not head:
            return head

        stack = []
        t = head

        while t:
            stack.append(t)
            t= t.next

        while n != 0:
            curr = stack.pop(-1)
            n -= 1
        if stack:
            prev = stack.pop(-1)
            prev.next = curr.next
        else:
            head = curr.next

        return head
