class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums.sort()
        x = nums[0]
        for i in range(1, len(nums)-1):
            if x == nums[i]:
                res.append(x)
            x = nums[i]
        return res


