class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        while head != None and head.val == val:
            head = head.next

        if not head:
            return head

        tmp = head
        np = head.next

        while np and tmp:
            if np.val == val:
                tmp.next = np.next
                np = np.next
            else:
                tmp.next = np
                tmp = tmp.next
                np = tmp.next

        return head
