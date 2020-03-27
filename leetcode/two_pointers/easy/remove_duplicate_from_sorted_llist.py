class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = head
        if not head:
            return head

        lp = head.next

        while lp:
            if res.val != lp.val:
                res.next = lp
                res = res.next
            lp = lp.next
        res.next = None
        return head
