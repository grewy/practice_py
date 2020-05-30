"""
452 min num of arrows to burst ballons
"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda x: x[1])

        shots = 1
        last_shot = points[0][1]

        for x in range(1, len(points)):
            if points[x][0] > last_shot:
                shots += 1
                last_shot = points[x][1]
        return shots


