# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        even_head = head.next
        odd_head = head
        tmp = odd_head
        tmp1 = even_head

        t = None
        if even_head:
            t= even_head.next
            even_head.next = None
            odd_head.next = None


        is_even = 0
        while t:
            x = t
            t = t.next
            x.next = None
            if not is_even:
                odd_head.next = x
                odd_head = odd_head.next
            else:
                even_head.next = x
                even_head = even_head.next

            is_even ^= 1



        odd_head.next = tmp1


        return tmp


