# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None

        if not l1 and l2:
            return l2
        if l1 and not l2:
            return l1
        if not l1 and not l2:
            return head

        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        head.next = None
        t = head

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2=l2.next
            head = head.next

        if not l1 and l2:
            head.next = l2
        elif l1 and not l2:
            head.next = l1

        return t

