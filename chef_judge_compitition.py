
for i in range(int(raw_input())):
  n = int(raw_input())

  al = map(int, raw_input().split())
  bob = map(int, raw_input().split())

  al.remove(max(al))
  bob.remove(max(bob))
  als = sum(al)
  bobs = sum(bob)
  if als < bobs:
    print "Alice"
  elif als == bobs:
    print "Draw"
  else:
    print "Bob"