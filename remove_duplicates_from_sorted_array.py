def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        rt = 1
        for lt in range(1, len(nums)):
            if nums[lt] != nums[lt-1]:
                nums[rt] = nums[lt]
                rt += 1
        return rt

