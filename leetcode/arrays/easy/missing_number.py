class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        xr = 0

        for i in range(1, n+1):
            xr ^= i
        for i in nums:
            xr ^= i

        return xr
