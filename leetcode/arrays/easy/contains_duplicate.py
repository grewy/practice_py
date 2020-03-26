class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        st = set(nums)
        if len(st) < len(nums):
            return True
        else:
            return False

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        for x,y in enumerate(nums[1:]):
            if y == nums[x]:
                return True
        return False

