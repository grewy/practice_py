def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        nums_orig = [x for x in nums]
        nums.sort()
        res = []
        while l < r:
            sm = nums[l] + nums[r]
            if sm == target:
                if nums[l] != nums[r]:
                    return [nums_orig.index(nums[l]), nums_orig.index(nums[r])]
                else:
                    l = nums_orig.index(nums[l])
                    return [l, nums_orig.index(nums[r], l+1)]
            elif sm < target:
                l += 1
            else:
                r -= 1
