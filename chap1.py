#R1.1 Write a short Python function, is multiple(n, m), that takes two integer
#values and returns True if n is a multiple of m, that is, n = mi for some
#integer i, and False otherwise.

def isMultiple(n, m):
  return (n%m==0)


#R1.2 Write a short Python function, is even(k), that takes an integer value and
#returns True if k is even, and False otherwise. However, your function
#cannot use the multiplication, modulo, or division operators

def isEven(k):
  if (-1) ** k  == 1:
    return True
  else:
    return False

#R1.3 Write a short Python function, minmax(data), that takes a sequence of
#one or more numbers, and returns the smallest and largest numbers, in the
#form of a tuple of length two. Do not use the built-in functions min or
#max in implementing your solution.


def minmax(arr):
  arr = sorted(arr)
  return (arr[0], arr[-1])


#R1.4 Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the positive integers smaller than n.

def sumSquares(n):
  return sum([x**2 for x in xrange(n)])

#R1.5 Give a single command that computes the sum from Exercise R-1.4, relying
#on Python s comprehension syntax and the built-in sum function.

#R1.6 Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the odd positive integers smaller than n.

#C-1.14 Write a short Python function that takes a sequence of integer values and
#determines if there is a distinct pair of numbers in the sequence whose
#product is odd.

def productOdd(arr):
  a = set(arr)
  n = len(a)
  b = list(a)
  for x in xrange(n):
    for y in xrange(x+1,n):
      if (b[x] * b[y]) % 2 != 0:
        return True
  return False

#Write a Python function that takes a sequence of numbers and determines
#if all the numbers are different from each other (that is, they are distinct)

def isDistinct(arr):
  a = {}
  for x in arr:
    if x in a.keys():
      return False
    else:
      a[x] = 1
  return True


#C-1.25 Write a short Python function that takes a string s, representing a sentence,
#and returns a copy of the string with all punctuation removed. For example,
#if given the string "Let's try, Mike.", this function would return
#"Lets try Mike".

def removePunc(s):
  punc = [',','.']
  a = list(s)
  for x in xrange(len(a)):
    if a[x] in punc:
      a[x] = '-'
  return ''.join(filter(lambda b: b != '-', a))


#P-1.29 Write a Python program that outputs all possible strings formed by using
#the characters c , a , t , d , o , and g exactly once.

def all_strings(arr):
  a = list(arr)
  import itertools
  return [''.join(x) for x in itertools.permutations(a)]


#P-1.30 Write a Python program that can take a positive integer greater than 2 as
#input and write out the number of times one must repeatedly divide this
#number by 2 before getting a value less than 2.

def value2(n):

  if n<2:
    return 0
  else:
    return 1+value2(n/2)

#