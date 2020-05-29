class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = len(nums) + 1
        l, r = 0, 0
        sm = 0
        found = False
        while r < len(nums):
            sm += nums[r]
            while sm >= s and l <= r:
                ans = min(ans, r-l+1)
                if ans == 1:
                    return ans
                sm -= nums[l]
                l += 1
                found = True
            r += 1

            if found:
                sm -= nums[l]
                l += 1

        return ans if ans < len(nums) + 1 else 0



