"""
Swap elements across diagonal and then across horizonatl/rows swap
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix[0])

        for i in range(length-1):
            for j in range(length-i):
                matrix[i][j], matrix[length-1-j][length-1-i] = matrix[length-1-j][length-1-i], matrix[i][j]

        for i in range(length/2):
            for j in range(length):
                matrix[i][j], matrix[length-i-1][j] = matrix[length-i-1][j], matrix[i][j]

