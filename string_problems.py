from itertools import permutations

from decorators import timing

def isPalindrome(s):
  return (s == s[::-1])

@timing
def getMaxLenOfPalindrome(s):
  count = {}
  for i in s:
    count[i] = count.get(i, 0) + 1
  palin_len = 0
  for k,v in count.items():
    if v%2 == 0:
      palin_len += v
    elif v%2 !=0 and v > 1:
      palin_len += v - 1
  return palin_len + 1


@timing
def largestPalin(s):
  n = len(s)
  #print s
  for i in range(n,1, -1):
    for j in permutations(s,i):
      x = ''.join(j)
      #print x
      if isPalindrome(x):
        return x, i

@timing
def largestPalin1(s):
  n = getMaxLenOfPalindrome(s)
  for i in permutations(s, n):
    x = ''.join(i)
    # print x
    if isPalindrome(x):
      return x, n

@timing
def findLongestPalindromicString(text):
    N = len(text)
    if N == 0:
      return
    N = 2 * N + 1  # Position count
    L = [0] * N
    L[0] = 0
    L[1] = 1
    C = 1  # centerPosition
    R = 2  # centerRightPosition
    i = 0  # currentRightPosition
    iMirror = 0  # currentLeftPosition
    maxLPSLength = 0
    maxLPSCenterPosition = 0
    start = -1
    end = -1
    diff = -1

    # Uncomment it to print LPS Length array
    # printf("%d %d ", L[0], L[1]);
    for i in xrange(2, N):

      # get currentLeftPosition iMirror for currentRightPosition i
      iMirror = 2 * C - i
      L[i] = 0
      diff = R - i
      # If currentRightPosition i is within centerRightPosition R
      if diff > 0:
        L[i] = min(L[iMirror], diff)

      # Attempt to expand palindrome centered at currentRightPosition i
      # Here for odd positions, we compare characters and
      # if match then increment LPS Length by ONE
      # If even position, we just increment LPS by ONE without
      # any character comparison
      try:
        while ((i + L[i]) < N and (i - L[i]) > 0) and \
            (((i + L[i] + 1) % 2 == 0) or \
             (text[(i + L[i] + 1) / 2] == text[(i - L[i] - 1) / 2])):
          L[i] += 1
      except Exception as e:
        pass

      if L[i] > maxLPSLength:  # Track maxLPSLength
        maxLPSLength = L[i]
        maxLPSCenterPosition = i

      # If palindrome centered at currentRightPosition i
      # expand beyond centerRightPosition R,
      # adjust centerPosition C based on expanded palindrome.
      if i + L[i] > R:
        C = i
        R = i + L[i]

    # Uncomment it to print LPS Length array
    # printf("%d ", L[i]);
    start = (maxLPSCenterPosition - maxLPSLength) / 2
    end = start + maxLPSLength - 1

    return text[start:end + 1]

def removeAdjacentSameChar(s):
  s= list(s)
  j = 0
  for i in range(1,len(s)):
    if s[i] != s[j]:
      j += 1
      s[j] = s[i]
  return ''.join(s[:j+1])




#s ="abababaavdsdddddddeeeeeeeefffdds"
#print findLongestPalindromicString(s)
#print getMaxLenOfPalindrome(s)

s = "ABCCBCBAABABAABBB"   #ABCBCBA
print removeAdjacentSameChar(s)

