class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_ = {}
        for idx, val in enumerate(nums):
            rem = target - val
            if rem not in nums_:
                nums_[val] = idx
            else:
                return [nums_[rem], idx]
