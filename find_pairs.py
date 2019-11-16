def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        a = []

        nums = Counter(nums)
        b = sorted(nums.keys())

        for i in b:
            if i+k in nums and nums[i+k] > 0 and k > 0:
                nums[i+k] -= 1
                a.append((i, i+k))
            elif k == 0:
                if nums[i] >= 2:
                    nums[i] -= 2
                    a.append((i ,i))
        return len(set(a))
