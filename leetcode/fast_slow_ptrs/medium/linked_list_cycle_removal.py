
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast is not None:
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            slow = slow.next
            if slow == fast:
                break

        if fast is None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow



