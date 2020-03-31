class Solution(object):
    def binarySearch(self, row, target):
        left, right = 0, len(row)-1

        while left <= right:
            mid = left + (right - left) / 2
            mid_value = row[mid]
            if target > mid_value:
                left = mid+1
            elif target < mid_value:
                right = mid-1
            else:
                return True

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or not len(matrix[0]):
            return False

        for x in matrix:
            if self.binarySearch(x, target):
                return True

        return False

