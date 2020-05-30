"""
424. Longest Repeating Character Replacement
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0

        l = 0

        mem = [0]*26
        for r, v in enumerate(s):
            mem[ord(v) - ord('A')] += 1
            max_chars = max(mem)

            if (r - l +1) - max_chars > k:
                mem[ord(s[l]) - ord('A')] -= 1
                l += 1

        return r - l + 1


