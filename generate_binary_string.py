from collections import deque


def gen_binary_string(arr, ch='?'):

  q = deque()
  q.append(arr)

  while len(q) > 0:
    s = list(q.popleft())
    if ch in s:
     idx = s.index(ch)
     s[idx] = '0'
     q.append(''.join(s))
     s[idx] = '1'
     q.append(''.join(s))
    else:
      print "".join(s)




gen_binary_string("1??0?101")
print "======================="
gen_binary_string("1?1?")
