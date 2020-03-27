class Solution(object):
    def reverse_ll(self, head):
        prev = None
        current = head
        while(current is not None):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        head = prev
        return head

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or (head and not head.next):
            return True

        if not head.next.next:
            if head.val == head.next.val:
                return True
            else:
                return False

        slow = head
        fast = slow

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = self.reverse_ll(slow)

        while list2:
            if head.val == list2.val:
                head = head.next
                list2 = list2.next
            else:
                return False


        return True
