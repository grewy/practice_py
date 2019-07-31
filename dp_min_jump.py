def minJumps(arr, n):
  # Find the minimum number of jumps to reach arr[i] from arr[0]
  # and assign this value to jumps[i]
  jumps = [float('inf') for x in range(n)]
  jumps[0] = 0
  for i in range(1, n):
    for j in range(i):
      if j+arr[j]>=i:
        jumps[i] = min(jumps[i], jumps[j]+1)
  return jumps[-1]



# Driver Program to test above function
arr = [2, 2, 0, 2, 0, 9]
size = len(arr)
print('Minimum number of jumps to reach end is', minJumps(arr, size))