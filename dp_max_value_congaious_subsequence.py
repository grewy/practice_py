

def maxSumSubSequence(a):
  cursum = a[0]
  maxsum = a[0]
  st = 0
  end = 0
  mst = 0
  mend = 0

  for i in range(1, len(a)):
    if a[i] > cursum + a[i]:
      cursum = a[i]
      st = i
      end = i
    else:
      cursum += a[i]
      end += 1

    if maxsum < cursum:
      mst = st
      mend = end
      maxsum = cursum

  return maxsum, mst, mend

def maxSumWO3Consec(arr, n):
  sm = [0]*n
  sm[0] = arr[0]
  sm[1] = arr[0] + arr[1]
  sm[2] = max(sm[1], max(sm[0]+arr[2], arr[1]+arr[2]))

  for i in range(3,n):
    # skip a[i]. skip a[i-1]. skip a[i-2]
    sm[i] = max(max(sm[i-1], sm[i-2]+arr[i]), sm[i-3]+arr[i]+arr[i-1])
  return sm[n-1]

# Driver code
arr = [100, 1000, 100, 1000, 1]
n = len(arr)
print maxSumWO3Consec(arr, n)

# Driver function to check the above function
#a = [-2, -3, 4, -1, -2, 1, 5, -3]
#print"Maximum contiguous sum is", maxSumSubSequence(a)