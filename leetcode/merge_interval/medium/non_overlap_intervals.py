"""
435 Non-overlap intervals
"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) < 2:
            return 0

        ans = 0
        intervals.sort(key=lambda x: x[1])

        prev = float("-inf")
        ans = 0

        for interval in intervals:
            if interval[0] >= prev:
                prev = interval[1]
            else:
                ans += 1

        return ans
