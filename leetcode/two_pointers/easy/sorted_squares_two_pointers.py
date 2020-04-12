class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)

        pos = 0
        while pos < n and A[pos] < 0:
            pos += 1
        neg = pos -1

        ans =[]

        while neg >= 0 and pos < n:
            if A[neg]**2 < A[pos]**2:
                ans.append(A[neg]**2)
                neg -= 1
            else:
                ans.append(A[pos]**2)
                pos += 1

        while neg >=0:
            ans.append(A[neg]**2)
            neg -= 1

        while pos < n:
            ans.append(A[pos]**2)
            pos += 1

        return ans
