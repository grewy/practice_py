def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur_len = 1 if len(nums) > 0 else 0
        max_len = cur_len

        for k, v in enumerate(nums[1:], 1):
            if v > nums[k-1]:
                cur_len += 1
            else:
                cur_len = 1

            if max_len < cur_len:
                max_len = cur_len

        return max_len
