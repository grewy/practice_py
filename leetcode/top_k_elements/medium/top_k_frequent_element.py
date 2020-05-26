from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, n):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = [(v, k) for k,v in Counter(nums).items()]
        q = heap[:n]
        heapq.heapify(q)

        for h in heap[n:]:
            heapq.heappushpop(q, h)

        return [x[1] for x in q]

