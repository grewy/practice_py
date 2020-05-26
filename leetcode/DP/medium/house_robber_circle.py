class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def line_rob(nums):
            rob, nrob = 0, 0
            for num in nums:
                rob, nrob = nrob + num, max(rob, nrob)
            return max(rob, nrob)

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            # if first robbed, last need to be left
            # if first not robbed, last can be considered for rob
            return max(line_rob(nums[1:]), line_rob(nums[:-1]))

