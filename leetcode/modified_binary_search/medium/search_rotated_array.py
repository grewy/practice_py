class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        pivot = 0

        while nums[l] > nums[r]:
            mid = (l+r)//2
            if nums[l] > nums[mid]:
                r = mid
            elif nums[mid + 1] > nums[r]:
                l = mid + 1
            else:
                pivot = mid + 1
                break


        if target == nums[-1]:
            return len(nums) - 1
        elif target > nums[-1]:
            l = 0
            r = pivot - 1
        else:
            l = pivot
            r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1

