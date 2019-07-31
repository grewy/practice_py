
def count_bits(x):
  num_bits = 0
  while x:
    num_bits += x & 1
    x = x >> 1
  return num_bits


def even_odd(arr):
  even, odd = 0, len(arr) - 1
  while even < odd:
    if arr[even] % 2 == 0:
      even += 1
    else:
      arr[even], arr[odd] = arr[odd], arr[even]
      odd -= 1


def partition(arr, idx):
 pivot = arr[idx]
 smaller, equal, larger = 0, 0, len(arr) - 1
 while equal < larger:
   if arr[equal] < pivot:
     arr[smaller], arr[equal] = arr[equal], arr[smaller]
     smaller += 1
     equal += 1
   elif arr[equal] == pivot:
     equal += 1
   else:
     arr[equal], arr[larger] = arr[larger], arr[equal]
     larger -= 1

def is_palindrome(arr):
  return all(arr[i] == arr[~i] for i in range(len(arr)//2))


def int_to_string(x):
  is_negative = False
  if x < 0:
    x, is_negative = -x, True

  s = []
  while True:
    s.append(chr(ord('0') + x % 10))
    x //= 10
    if x == 0:
      break

  return ('-' if is_negative else '') + ''.join(s[::-1])


def gcd(a,b):
  if a == 0:
    return b
  else:
    return gcd(a%b,a)

def sum_list(arr, sum=0):
  if not arr:
    return sum
  else:
    sum += arr[0]
    return sum_list(arr[1:],sum)


def is_palin(s):
  if not s:
    return True
  if s[0] != s[-1]:
    return False
  else:
    return is_palin(s[1:-1])


def parts(arr, l, r):
  pivot = arr[r]
  i = l - 1
  for j in range(l,r):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[r] = arr[r], arr[i+1]
  return i+1

def evenodd(arr, l, r):
  while l < r:
    if arr[l]%2!=0 and arr[r]%2==0:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r -= 1
    elif arr[l] % 2 == 0:
      l += 1
    elif arr[r] % 2 != 0:
      r -= 1
#O(nlogn)
def elect(a):
  n = len(a)
  a.sort()
  ccd = a[0]
  mcd = a[0]
  cc = 1
  mc = 1
  for i in range(1,n):
    if ccd == a[i]:
      cc += 1
      if cc > mc:
        mc = cc
        mcd = ccd
    else:
      ccd = a[i]
      cc = 1
  return mcd

#O(n)
def elect1(a):
  idx = 0
  count = 0
  for i in range(len(a)):
    if a[i] == a[idx]:
      count += 1
    else:
      count -= 1
    if count == 0:
      idx = i
      count = 1
  return a[idx]

def sort012(a):
  z, o, t = 0,0,0
  for i in a:
    if i == 0:
      z+=1
    elif i ==1:
      o+=1
    else:
      t+=2
  for i in range(len(a)):
    if z > 0:
      a[i] = 0
      z -= 1
    elif o > 0:
      a[i] = 1
      o-=1
    else:
      a[i]=2
      t-=1

def sort0121(a, pivot=1):
  smaller, equal, larger = 0,0,len(a)-1
  while equal < larger:
    if a[equal] < pivot:
      a[smaller], a[equal] = a[equal], a[smaller]
      smaller+=1
      equal += 1
    elif a[equal] == pivot:
      equal+=1
    else:
      a[larger], a[equal] = a[equal], a[larger]
      larger -= 1

#check duplicate if values in 0-n
def dupcheck(a):
  n = len(a)
  for i in range(n):
    if a[abs(a[i])] < 0:
      return True
    else:
      a[abs(a[i])] = -a[abs(a[i])]
  return False

def firstoccurance(a, l, r, k):
  if l <= r:
    m = (l+r)/2
    if a[m]==k and a[m-1]<a[m]:
      return m
    elif a[m]>=k:
      return firstoccurance(a, l, m-1, k)
    else:
      return firstoccurance(a, m+1, r, k)

def max0row(a,n):
  i,cc,mc = [0]*3
  j = n-1
  idx = i
  while i < n and j>=0:
    if a[i][j] == 0:
      cc += 1
      j -=1
    else:
      if cc > mc:
        mc = cc
        idx = i
      i += 1
  return idx

# a1a2...anb1b2..bn ---> a1b1a2b2
def shuffle(a,l,r):
  if l < r:
    pass

def removedup(a):
  n = len(a)
  i,j = 0,0
  dct ={}
  while j < n:
    if dct.get(a[j],-1) == -1:
      dct[a[j]] = 1
      a[i] = a[j]
      i += 1
    j += 1
  return a[:i]

def median(a):
  n = len(a)
  if n%2 !=0:
    return a[n/2]
  else:
    return (a[n/2] + a[n/2 - 1])/2.0

def medianSortedArrays(a,b):
  n1 = len(a)
  n2 = len(b)
  m = (n1+n2)
  even = True if m%2==0 else False
  exp = m/2
  i, j = 0, 0
  p , c = -1, -1
  count = 0
  while i < n1 and j < n2 and count<=exp:
    if a[i] <= b[j]:
      p = c
      c = a[i]
      i += 1
    else:
      p = c
      c = b[j]
      j += 1
    count += 1
  if count==exp:
    if even:
     return (p+c)/2.0
    else:
      return c
  else:
    x = (i,n1) if i < n1 else j,n2
    i,n = x
    while i < n and count <=exp:
      p=c
      c=a[i]
      i+1
      count+=1
    if even:
     return (p+c)/2.0
    else:
      return c

def getMedianSortedArrays(a,b):
  m1 = median(a)
  m2 = median(b)

  if m1 == m2:
    return m1

  if len(a) == len(b) and len(a) == 2:
    return (max(a[0],b[0]) + min(a[1],b[1]) ) /2.0

  m1idx = len(a)/2
  m2idx = len(b)/2

  if m1 > m2:
    return getMedianSortedArrays(a[:m1idx+1], b[m2idx:])
  else:
    return getMedianSortedArrays(a[m1idx:], b[:m2idx+1])

def getLowestIndxRepeated(a,k):
  l, r = 0, len(a) - 1
  while l < r:

    m = (r+l)/2

    if a[l]==k:
      return l
    if a[m] == k and a[m-1] < a[m]:
      return m

    if a[m] >= k:
      r = m - 1
    else:
      l = m + 1

def shuffleAButil(a, l, r):

  if r-l == 1:
    return

  mid = int((l+r)/2)
  rmid = mid+1
  lmid = int((l+mid)/2)

  for i in range(lmid+1,mid+1):
    a[i], a[rmid] = a[rmid], a[i]
    rmid += 1

  shuffleAButil(a, l, mid)
  shuffleAButil(a, mid+1, r)

def shuffleAB(a,l,r):
  if (r/2 + 1) % 2 !=0 :
    # insert '#' at end of 'a' series and 'b' series if 'n' is odd
    a.append("#")
    a.append('#')
    mid = (l+r)/2
    for i in range(r+1,mid, -1):
      a[i+1] = a[i]
    a[i] = "#"
    r += 2

  shuffleAButil(a,l,r)
  return a[:-2] if "#" in a else a




a = [ [1,1,1,1], [1,1,0,0], [1,0,0,0], [1,1,0,0]]
arr= [ 1, 2, 3, 4, 4, 4, 7, 8, 9, 9, 9 ]
arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]
a = [1, 3, 5, 7, 2, 4, 6, 8]
ab = ['a1','a2','a3', 'a4','a5','a6','a7',
      'b1','b2','b3','b4','b5', 'b6', 'b7']

print ''.join(shuffleAB(ab, 0, len(ab)-1))



