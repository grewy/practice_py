def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]
