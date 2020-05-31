class Solution(object):
    def permute(self, nums):
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
                    visited.add(i)
                    backtrack(nums, visited, ans, subset + [nums[i]])
                    visited.remove(i)

        visited = set()
        ans = []

        backtrack(nums, visited, ans, [])
        return ans
