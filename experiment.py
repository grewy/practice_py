from decorators import timing
from itertools import chain, combinations

@timing
def substr1(data=None):
  data= 'abcdefghijklm' if data is None else data
  result = []
  for num in xrange(1,len(data)+1):
    for i in combinations(data,num):
      result.append(i)
  return set(result)

@timing
def substr2(data=None):
  data = 'abcdefghijklm' if data is None else data
  result = []
  for i in list(chain(*[combinations(data, x) for x in range(1, len(data) + 1)])):
    result.append(i)
  return set(result)

# contigous substrings
@timing
def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]





class api():
  def __init__(self):
    print "in api"

def foo():
  print "in foo"

a= api()

with a:
  foo()