class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #single element array
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        #array is not rotated
        if nums[r] > nums[l]:
            return nums[l]

        while l <= r:
            m = l + (r-l)/2

            # check if nums[m] is highest -> ans is next element
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            # check if nums[m] is lowest -> ans is nums[m]
            if nums[m-1] > nums[m]:
                return nums[m]
            # nums[l:m+1] is increasing part -> ans in nums[m+1:]
            if nums[m] > nums[l]:
                l = m + 1
            else:
                r = m - 1
