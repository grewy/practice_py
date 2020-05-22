def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = range(1, len(nums) + 1)
        for x in nums:
            res[x-1] = 0
        return filter(lambda x: x != 0, res)

print findDisappearedNumbers([1,2,3,5,5,5])
