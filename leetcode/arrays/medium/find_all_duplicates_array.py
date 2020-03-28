class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            index = nums[i]

            if index < 0:
                index = -index

            if nums[index - 1] < 0:
                res.append(index)
            else:
                nums[index-1] = -nums[index-1]

        return res
