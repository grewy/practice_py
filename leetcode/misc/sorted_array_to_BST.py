# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return

        l, r = 0, len(nums) - 1
        m = (l+r)//2

        node = TreeNode(nums[m])
        node.left = self.sortedArrayToBST(nums[l:m])
        node.right = self.sortedArrayToBST(nums[m+1:])

        return node
