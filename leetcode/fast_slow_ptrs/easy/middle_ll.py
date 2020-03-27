class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = slow

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
