
def LIS(ar, n):
  #lis[i] longest LIS from 0 to i
  lis = [1]*n
  for i in range(1,n):
    for j in range(i):
      if ar[i] > ar[j]:
        lis[i] = max(lis[j]+1, lis[i])
  return max(lis)




# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print "Length of lis is 5? ", LIS(arr, len(arr)) == 5