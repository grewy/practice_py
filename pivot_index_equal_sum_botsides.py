def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lsum = 0
        total_sum = sum(nums)

        for k, v in enumerate(nums):
            lsum += v
            rsum = total_sum - lsum
            if rsum == lsum - v:
                return k
        return -1
