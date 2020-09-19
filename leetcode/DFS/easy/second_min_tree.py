# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        first_min = -1
        second_min= -1

        stack = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()

                if first_min < 0:
                    first_min = cur.val
                else:
                    if cur.val < first_min:
                        second_min = first_min
                        first_min = cur.val
                    elif first_min < cur.val < second_min or first_min < cur.val and second_min == -1:
                        second_min = cur.val

                cur = cur.right

        return second_min
