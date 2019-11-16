def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonz = []
        for i in nums:
            if i != 0:
                nonz.append(i)

        for i in range(0, len(nonz)):
            nums[i] = nonz[i]
        for x in range(i+1, len(nums)):
            nums[x] = 0
