"""
Usage:
    python count_set_bits.py <num> <iterations> <method>
"""
import sys

from profile import profile

INT_BITS_NIBBLE = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]



def ones_1(num):
    count = 0
    while num:
        num &= num - 1
        count += 1
    return count


def ones_mem(num):
    nib = 0
    if num == 0:
        return INT_BITS_NIBBLE[0]
    nib = num & 0xf
    return INT_BITS_NIBBLE[nib] + ones_mem(num>>4)



if __name__ == '__main__':
    num = int(sys.argv[1])
    try:
        itr = int(sys.argv[2])
    except IndexError:
        itr = 1

    try:
        method = int(sys.argv[3])
    except IndexError:
        method = ones_1

    if method == 1:
        method = ones_1
    if method == 2:
        method = ones_mem

    for _ in xrange(itr):
        print "1s using : ", profile(method)(num)
