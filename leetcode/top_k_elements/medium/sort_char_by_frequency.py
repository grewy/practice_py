from collections import Counter
import heapq
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        heap = [(-v, k) for k, v in Counter(s).items()]
        heapq.heapify(heap)

        ans = ''

        while len(heap) > 0:
            times, ch = heapq.heappop(heap)
            times = -times

            ans += ch*times

        return ans
