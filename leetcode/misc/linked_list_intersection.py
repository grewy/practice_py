# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []

        while headA:
            stack1.append(headA)
            headA = headA.next
        while headB:
            stack2.append(headB)
            headB = headB.next

        inter = None
        while stack1 and stack2:
            if stack1[-1] != stack2[-1]:
                break
            else:
                inter = stack1.pop()
                stack2.pop()
        return inter



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB

        if p1 == p2:
            return p1

        turn = 0
        while p1 != p2 and p1 and p2 and turn < 2:


            p1 = p1.next
            if not p1:
                p1 = headB
                turn += 1

            p2 = p2.next
            if not p2:
                p2 = headA

            if p1 == p2:
                return p1
