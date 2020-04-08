class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]

        # heapq._heapify_max(nums)
        # for i in range(k-1):
        #     heapq._heappop_max(nums)
        # return heapq._heappop_max(nums)
