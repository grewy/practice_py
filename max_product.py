def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = nums[-2]*nums[-1]*nums[-3]
        ans1 = nums[0]*nums[1]*nums[2]
        if nums[0] < 0 and nums[1] < 0:
            ans1 = nums[0] * nums[1] * nums[-1]

        return ans if ans > ans1 else ans1
