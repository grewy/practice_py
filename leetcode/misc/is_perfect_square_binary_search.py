class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l <= r:
            m = (l+r)//2
            if m*m == num:
                return True
            elif m*m > num:
                r = m -1
            else:
                l = m +1
        return False


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            m = (l+r)//2
            if m*m == x:
                return m
            if m*m > x:
                r = m -1
            else:
                l = m+ 1
        return r
