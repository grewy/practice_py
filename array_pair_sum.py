class Solution(object):
    def get_sum(self, nums):
        """
        Doc
        """
        res = 0
        n = len(nums)
        evs = [nums[x] for x in range(n) if x % 2 == 0]
        ods = [nums[x] for x in range(n) if x % 2 != 0]
        return sum(min(evs[x], ods[x]) for x in range(n/2))


    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        neg = []
        res = 0

        res += self.get_sum(nums)

        return res
