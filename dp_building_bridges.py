from operator import itemgetter
from dp_LIS import LIS

def builBridges(ar,n):
  ar = sorted(ar, key=itemgetter(0))
  a = [x[1] for x in ar]
  return LIS(a, len(a))





#Driver
ar = [(6, 2), (4, 3), (2, 6), (1, 5)]
print builBridges(ar, len(ar))

