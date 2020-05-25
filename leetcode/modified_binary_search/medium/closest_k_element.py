
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
