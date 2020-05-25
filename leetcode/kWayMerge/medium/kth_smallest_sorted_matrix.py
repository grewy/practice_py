"""
378. Kth Smallest Element in a Sorted Matrix
"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return -1

        import heapq
        heap = []
        for r in matrix:
            for c in r:
                if len(heap) < k:
                    heapq.heappush(heap, -c)
                elif c < -heap[0]:
                    heapq.heappushpop(heap, -c)
        return -heap[0]

