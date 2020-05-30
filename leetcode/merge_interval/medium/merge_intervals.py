"""
56. Merge intervals
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[1])

        r = len(intervals) - 1

        while r > 0:
            if intervals[r-1][1] >= intervals[r][0]:
                x = min(intervals[r][0], intervals[r-1][0])
                y = max(intervals[r][1], intervals[r-1][1])
                intervals.pop(r)
                intervals.pop(r-1)
                intervals.insert(r-1, [x, y])

            r -= 1

        return intervals
