# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
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
