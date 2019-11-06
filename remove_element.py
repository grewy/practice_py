class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)

        l, r = 0, len(nums) - 1
        while l < r:

            if nums[r] != val:
                if nums[l] == val:
                    nums[l], nums[r] = nums[r], nums[l]
                    r -= 1
                l += 1
            else:
                if nums[l] == val:
                    r -= 1
                else:
                    l += 1
                    r -= 1

        return nums.index(val)
