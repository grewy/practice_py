class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, r = 0, len(A) - 1

        while l <= r:
            mid = l + (r - l)/2

            if A[mid-1] < A[mid] and A[mid] > A[mid+1]:
                return mid

            elif A[mid-1] < A[mid] and A[mid] < A[mid+1]:
                l = mid+1

            elif A[mid] > A[mid+1] and A[mid-1] > A[mid]:
                r = mid -1

        return -1
