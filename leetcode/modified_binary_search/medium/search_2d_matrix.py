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

        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows -1
        while l <= r:
            m = l + (r-l)/2
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                return self.binarySearch(matrix[m], target)
            elif matrix[m][-1] < target:
                l = m+1
            else:
                r = m-1

        return False
