"""
Given an array of size n-1 and given that there are numbers from 1 to n with one missing,
the missing number is to be found.
"""

def get_missing_number(ar):
    ar_len = len(ar)
    xr = 1
    for i in range(2, ar_len+2):
        xr ^= i
    for i in ar:
        xr ^= i
    return xr


# Test
print get_missing_number([1,2,3,5])
print get_missing_number([1,2,3,4,5,6,7,8,10])
