def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import math
        if not nums or k < 0:
                return 0
        from collections import Counter
        res = 0

        nums = Counter(nums)

        for i in nums.keys():
            if k == 0 and nums[i] > 1:
                res += 1
            elif k != 0:
                if i+k in nums:
                    res += 1
                if i-k in nums:
                    res += 1

        if k != 0 and res > 1:
            res = res/2

        return res
