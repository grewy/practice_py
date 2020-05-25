"""
Case 1. p*x < k
This means we can move the window’s right bound one step further. How many contiguous arrays does this step produce? It is: 1 + (end-start).

Indeed, the element itself comprises an array, and also we can add x to all contiguous arrays which have right border at end. There are as many such arrays as the length of the window.

Case 2. p*x >= k

This means we must first adjust the window’s left border so that the product is again less than k. After that, we can apply the formula from Case 1.


https://www.geeksforgeeks.org/number-subarrays-product-less-k/
"""

class Solution(object):
    def numSubarrayProductLessThanK(self, a, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(a)
        p = 1
        res = 0
        start = end = 0
        while(end < n):
            p *= a[end]

            while (start < end and p >= k):
                p =int(p//a[start])
                start+=1

            if (p < k):
                res += end - start + 1

            end+=1

        return res

