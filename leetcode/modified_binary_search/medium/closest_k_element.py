
def closest(arr, k, x):
    """
    K count of closest numbers
    x is closest to
    """
    arr = sorted(arr, key=lambda y: abs(x-y))
    return sorted(arr)[:k]

def closest_binary_search(arr, k, x):
    l, r  = 0, len(arr) - k

    while l < r:
        mid = l + (r-l) // 2

        if x - arr[mid] > arr[mid+k] - x:
            l = mid +1
        else:
            r = mid
    return a[l:l+k]


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]
        else:
            l, r = 0, len(arr) - k

            while l < r:
                m = l + (r-l)//2
                if x - arr[m] > arr[m+k] - x:
                    l = m+1
                else:
                    r = m
            return arr[l:l+k]
