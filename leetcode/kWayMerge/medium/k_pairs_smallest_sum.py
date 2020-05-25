class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        import heapq
        heap = []
        for i in nums1:
            for j in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-(i+j), i , j))
                elif (i+j) < -heap[0][0]:
                    heapq.heappushpop(heap, (-(i+j), i , j))

        return [[x[1], x[2]] for x in heap]

