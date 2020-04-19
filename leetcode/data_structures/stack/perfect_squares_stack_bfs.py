"""
https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/discuss/71475/Short-Python-solution-using-BFS
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        # populate probable squares
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1

        cnt = 0
        stack = set([n])
        while stack:
            cnt += 1
            nstack = set()
            while stack:
                temp = stack.pop()
                for y in lst:
                    if y == temp:
                        return cnt
                    if temp < y:
                        break
                    nstack.add(temp-y)
            stack = nstack

        return cnt
