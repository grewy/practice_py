class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)


        l , r = 0, len(nums) - 1

        while l <= r:

            mid = l + (r-l)/2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        l , r = 0, len(nums) - 1


        while l <= r:
            mid = l + (r-l)/2

            if nums[mid] < target and nums[mid+1] > target:
                return mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return 0
