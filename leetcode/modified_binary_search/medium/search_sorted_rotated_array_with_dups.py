class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2

            if target == nums[m]:
                return True

            # skip all nums[l] duplicate
            while l < m and nums[l] == nums[m]:
                l += 1

            # first part is sorted
            if nums[l] <= nums[m]:
                # if in first sorted half
                if nums[l] <= target < nums[m]:
                    r = m -1
                else:
                    l = m + 1
            # if 2nd part is sorted part
            else:

                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False


