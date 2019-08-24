

def string_rotate(s, t):
    ss = s + s
    tt = t + t
    if s in tt and t in ss:
        return True
    else:
        return False

s = raw_input()
t = raw_input()
if string_rotate(s, t):
    print "Yes"
else:
    print "No"
