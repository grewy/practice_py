
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return -1

    res = 0
    for i in range(k):
        res += arr[i]

    curr_sum = res
    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i-k]
        res = max(res, curr_sum)
    return res

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print max_sum_subarray(arr, k)
