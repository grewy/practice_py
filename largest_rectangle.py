#!/bin/python

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    s = []
    max_area = 0
    i = 0
    while i < len(h):
        if not s or h[i] >= h[s[-1]]:
            s.append(i)
            i += 1
        else:
            top = s.pop(-1)
            area = h[top]*((i - s[-1]- 1) if s else i)
            max_area = max(area, max_area)

    while s:
        tp = s.pop(-1)
        area = h[tp]*((i-s[-1] -1) if s else i)
        max_area = max(area, max_area)

    return max_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    h = map(int, raw_input().rstrip().split())

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
