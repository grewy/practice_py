class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for ch in s:
            try:
                idx = t.index(ch)
            except ValueError:
                return False
            t = t[idx+1:]
        return True
