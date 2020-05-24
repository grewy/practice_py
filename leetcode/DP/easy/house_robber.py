"""
198. House robber
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r, nr  = 0, 0
        for n in nums:
            r, nr = nr + n, max(r, nr)
        return max(r, nr)


