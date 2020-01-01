def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l+r)/2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            elif mid_val < target:
                l += 1
            else:
                r -= 1

        return -1
