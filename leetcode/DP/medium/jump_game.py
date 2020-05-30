class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        can_reach, n = 0, len(nums)
        for i, x in enumerate(nums):
            # cant reach current index from last max jump, return False
            if can_reach < i:
                return False
            if can_reach >= n - 1:
                return True
            can_reach = max(can_reach, i + x)

