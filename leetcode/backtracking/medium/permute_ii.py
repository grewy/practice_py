class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums, visited, ans, subset):

            if len(subset) == len(nums):
                ans.append(subset)
                return

            for i in range(len(nums)):
                if i not in visited:
                    if i >0 and nums[i] == nums[i-1] and i-1 not in visited:
                        continue

                    visited.add(i)

                    backtrack(nums, visited, ans, subset + [nums[i]])
                    visited.remove(i)


        visited = set()
        ans = []
        nums.sort()
        backtrack(nums, visited, ans, [])
        return ans

