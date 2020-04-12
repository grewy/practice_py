# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = None

        carry = 0
        while l1 and l2:
            sm = l1.val + l2.val + carry
            carry = sm / 10
            sm = sm % 10

            n = ListNode(sm)
            if res:
                res.next = n
                res = res.next
            else:
                res = n
                head = res

            l1 = l1.next
            l2 = l2.next

        if not carry:
            if l1:
                res.next = l1
            if l2:
                res.next = l2
        else:
            while l1:
                l1.val += carry
                carry = l1.val / 10
                l1.val = l1.val % 10
                res.next = l1
                res = res.next
                l1 = l1.next

            while l2:
                l2.val += carry
                carry = l2.val / 10
                l2.val = l2.val % 10
                res.next = l2
                res = res.next
                l2 = l2.next

        if not l1 and not l2 and carry:
                res.next = ListNode(carry)

        return head


