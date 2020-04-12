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
        if not head or not head.next:
            return

        slow = head
        fast = head

        slow = slow.next
        fast = fast.next.next

        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next


        if not fast or not fast.next:
            return

        slow = head

        while slow != fast:
            slow= slow.next
            fast = fast.next

        return slow



