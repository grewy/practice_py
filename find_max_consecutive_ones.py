def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_count = 0
        max_so_far = 0
        for i in nums:
            if i == 1:
                cur_count += 1
                if cur_count > max_so_far:
                    max_so_far =cur_count
            else:
                cur_count = 0

        return max_so_far
