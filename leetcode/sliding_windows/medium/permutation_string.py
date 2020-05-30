"""
567. permutation string
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False

        s1map = [0]*26
        s2map = [0]*26
        l, r = 0, 0
        while r < len(s1):
            s1map[ord(s1[r]) - ord('a')] += 1
            s2map[ord(s2[r]) - ord('a')] += 1
            r += 1

        if s1map == s2map:
            return True

        while r < len(s2):
            s2map[ord(s2[r]) - ord('a')] += 1
            s2map[ord(s2[l])- ord('a')] -= 1
            l += 1
            r += 1

            if s1map == s2map:
                return True

        return False
