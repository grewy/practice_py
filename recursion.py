def gcd(a,b):
  if a == 0:
    return b
  else:
    return gcd(a%b,a)

def sum_list(arr):
  if len(arr) == 1:
    return arr[0]
  else:
    return arr[0] + sum_list(arr[1:])

def is_palin(s):
  if not s:
    return True
  if s[0] != s[-1]:
    return False
  else:
    return is_palin(s[1:-1])

def print_list(arr):
  if not arr:
    return
  else:
    print arr[0],
    print_list(arr[1:])

def print_reverse_list(arr):
  if not arr:
    return
  else:
    print_reverse_list(arr[1:])
    print arr[0],

def count_even(arr,count=0):
  if not arr:
    return count
  else:
    if arr[0] % 2 == 0:
      count += 1
    return count_even(arr[1:], count)

def fibo(n):
  if n < 0:
    return
  if n == 1 or n==2:
    return 1
  else:
    return fibo(n-1) + fibo(n-2)

def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n-1)

def find_num(arr, k):
  if len(arr) == 1:
    return (arr[0]==k)
  else:
    return (arr[0]==k) or find_num(arr[1:], k)

def binary_search(arr, k):
  if not arr:
    return False
  else:
    mid = (0+len(arr)-1)/2
    if arr[mid] == k:
      return True
    elif arr[mid] > k:
      return binary_search(arr[:mid], k)
    else:
      return binary_search(arr[mid+1:], k)


def


#####################################################

def bin(n):

  if n==0:
    return
  bin(n/2)
  print n%2,



######################################################

def log2(n):
  if n==1:
    return 0
  else:
    return 1+log2(n/2)




#######################################################

def fact(n):

  if n<=1:
    return 1
  else:
    return n*fact(n-1)




########################################################

#Equal sum array partition excluding a given element
#Given an array arr[] and an index in it. Find whether
# the array arr[] can be partitioned into two disjoint
# sets such that sum of both the sets is equal and none
# of the sets includes arr[index]


def canPartition(arr, idx):
  sm = 0
  for i, val in enumerate(arr):
    if i != idx:
      sm += val

  return (sm%2==0 and isSubsetSumPossible(arr, 0, 0, 0, idx,0))

def isSubsetSumPossible(arr, n, s1, s2, idx, pos):

  if pos == n:
    return (s1==s2)

  if pos == idx:
    isSubsetSumPossible(arr,n, s1, s2, idx, pos+1)

  return isSubsetSumPossible(arr, n, s1+arr[pos], s2,idx, pos+1) or \
         isSubsetSumPossible(arr, n, s1, s2 + arr[pos], idx, pos + 1)

