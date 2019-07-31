#!/usr/bin/python
"""
Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.
"""

class KadaneAlgo(object):

    def __init__(self, array):
        self._list = array

    def max_sum_subarray(self):
        sum_so_far = self._list[0]
        max_sum = self._list[0]
        for i in range(1, len(self._list)):
            sum_so_far = max(self._list[i], sum_so_far + self._list[i])
            max_sum = max(sum_so_far, max_sum)
        return max_sum


# Test
print KadaneAlgo([1,2,3]).max_sum_subarray()
print KadaneAlgo([-1, -2, -3, -4]).max_sum_subarray()

