class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [nums[0]]
        lnp = 1

        for i in range(1, len(nums)):
            l, r = 0, len(dp) - 1

            while l < r:
                m = (l+r)//2

                if dp[m] < nums[i]:
                    l = m + 1
                else:
                    r = m

            if dp[l] < nums[i]:
                dp.append(nums[i])
                lnp += 1
            else:
                dp[l] = nums[i]

        return lnp

