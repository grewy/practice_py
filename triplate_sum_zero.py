
def triplate_sum_zero(arr):

  arr_len = len(arr)
  if arr_len < 3:
    return False

  arr.sort()

  #first and last in sorted arr should be of opposite sign atleast
  if not ((arr[0] ^ arr[-1]) < 0):
    return False

  high = arr_len - 1
  for k,v in enumerate(arr[:-2]):
    sm = -v
    low = k+1

    while low < high:
      lh_sum = arr[low] + arr[high]
      if lh_sum == sm:
        return True
      elif lh_sum < sm:
        low += 1
      else:
        high -= 1
  return False

print triplate_sum_zero([10,2, 1, -3, 0])
print triplate_sum_zero([1,2])
print triplate_sum_zero([0,0,0,0,0,0])
print triplate_sum_zero([1,2,3])
print triplate_sum_zero([-1,-2,-3])
print triplate_sum_zero([0,10,-1,2])