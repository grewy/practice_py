
def division(dividend, divisor):
  quotient = 0
  while dividend >= divisor:
    dividend -= divisor
    quotient += 1
  # round off
  if dividend > (divisor >> 1):
    return quotient + 1
  return quotient

def list_mul(a):
  return reduce(lambda x, y: x*y, a)

def array_mul_without_element(ar):
  lst_ml = list_mul(ar)
  res = []
  for i in ar:
    res.append(division(lst_ml, i))
  return res


print array_mul_without_element([1, 2, 3, 4, 5])
