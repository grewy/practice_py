class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xr = 0
        for x in nums:
            xr ^= x
        return xr
