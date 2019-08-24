"""
B - String Rotation
Time Limit: 2 sec / Memory Limit: 1024 MB

Score :
200
 points

Problem Statement
You are given string
S
 and
T
 consisting of lowercase English letters.

Determine if
S
 equals
T
 after rotation.

That is, determine if
S
 equals
T
 after the following operation is performed some number of times:

Ex.
kyoto & tokyo
In the first operation, kyoto becomes okyot.
In the second operation, okyot becomes tokyo.
"""
def is_anargam(s, t):
    if sorted(s.lower()) == sorted(t.lower()):
        return True
    else:
        return False


def string_rotate(s, t):
    """
    check if strings equal after roatation
    """
    if s==t:
        return True

    if not is_anargam(s, t):
        return False

    idx = s.index(t[0])
    f_part = s[idx:]
    l_part = s[:idx]

    if f_part + l_part == t:
        return True
    else:
        return False


s = raw_input()
t = raw_input()

if string_rotate(s, t):
    print "Yes"
else:
    print "No"
