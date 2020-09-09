class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #_min & _max in unsorted array
        _min = float('inf')
        _max = float('-inf')

        flag = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                flag = True
            if flag:
                _min = min(_min, nums[i])

        flag = False
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                flag = True
            if flag:
                _max = max(_max, nums[i])

        #find correct position of _min and _max
        l, r = 0, len(nums) - 1
        while l < len(nums):
            if _min < nums[l]:
                break
            l += 1

        while r >= 0:
            if _max > nums[r]:
                break
            r -= 1

        return r-l+1 if r-l > 0 else 0



class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums)
        start = len(nums) - 1
        end = 0
        for i in range(len(nums)):
            if nums_sorted[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)
        return end - start +1 if end - start > 0 else 0

