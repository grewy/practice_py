class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        if nums[r] > nums[l]:
            return nums[l]

        while l <= r:
            m = l + (r-l)/2

            if nums[m] > nums[m + 1]:
                return nums[m + 1]

            if nums[m-1] > nums[m]:
                return nums[m]

            if nums[m] > nums[0]:
                l = m + 1
            else:
                r = m - 1
