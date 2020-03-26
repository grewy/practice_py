class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = range(1, len(nums) + 1)
        for x in nums:
            res[x-1] = 0
        return [x for x in res if x != 0]
