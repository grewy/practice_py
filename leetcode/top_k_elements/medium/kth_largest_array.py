class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []

        heap = []
        for num in nums:
            heapq.heappush(heap, num)

        for _ in range(len(nums)-k):
            heapq.heappop(heap)

        return heapq.heappop(heap)
