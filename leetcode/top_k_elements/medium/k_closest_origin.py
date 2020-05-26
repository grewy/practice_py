import heapq
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not points:
            return []

        def dist(x):
            return sqrt( (x[0] - 0)**2 + (x[1] - 0)**2 )

        ch =[]
        for p in points:
            ch.append((-dist(p), p))
        heapq.heapify(ch)


        for _ in range(len(points) - K):
            heapq.heappop(ch)

        return [x[1] for x in ch]


import heapq
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not points:
            return []

        heap = []

        for x,y in points:
            d = -(x*x+y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (d, [x,y]))
            else:
                heapq.heappush(heap, (d, [x,y]))

        return [x[1] for x in heap]
