def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dt = {}
        for i, v in enumerate(nums):
            if v not in dt:
                dt[v] = [i]
            else:
                if len(dt[v]) > 0 and i - dt[v][-1] <= k:
                    return True
                dt[v].append(i)
        return False
