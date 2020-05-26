"""
For a case that is build on this one e.g 'aaaabbc'. For 4 'a's we use 2 'b's to form 'abab'('ab'*2) to reduce this 3 letters problem to a 2 letters problem 'aac'. So we are back in the easy case and this give us an idea to solve the problem by induction.

General method
For a given string, we can always rearrange it in the form 'aaaabbbccd',i.e decending trend in the numebr of occurence. We want to use the letter with most occurence to remove the letter that has the second most occurence. Do the same for the remaining string and continue this process until we are back to the simple case where we can determine the result easily.

Keep in mind the 'aaaabbbccd' structure. When we have removed all other letters, we are left with one letter. If the remaining occurence is one then we can put it at the very end e.g xxxxxxaba. If not(i.e more than one), then it is impossible to rearrange to the desired structure and return ''.

reason to use heap
Occurence suggest we need to count the number of occurence for each letter. Frequent removal of letter with high prioirity suggest priority queue as data structure and hence a heap in this case.
"""
from collections import Counter
import heapq
def reorg(s):
    ans = ''
    ch = [(-v,k) for k,v in Counter(s).items()]
    heapq.heapify(ch)
    while ch:
        n, cur = heapq.heappop(ch)
        n = -n
        if not ch:
            if n == 1:
                ans += cur
                return ans
            else:
                return ''

        m, fill = heapq.heappop(ch)
        m = -m
        ans += (cur+fill)*m
        if n < m:
            heapq.heappush(ch, (-(n-m), cur))

    return ans
