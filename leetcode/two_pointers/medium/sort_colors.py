class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        l, k, r = 0, 0, len(nums) - 1


        while  k <= r:

            if nums[k] == 0:
                nums[k], nums[l] = nums[l], nums[k]
                l += 1
                k += 1
            elif nums[k] == 1:
                k += 1
            else:
                nums[k], nums[r] = nums[r], nums[k]
                r -= 1









