# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def get_length(head):
            t = head
            n = 0
            while t:
                n += 1
                t = t.next
            return n

        n = get_length(head)

        if n <= 1:
            return head

        k = k % n
        if k == 0:
            return head

        slow = head
        for _ in range(n-k-1):
            slow = slow.next

        prev = curr = slow.next
        slow.next = None
        while curr.next:
            curr = curr.next

        curr.next = head
        return prev


