def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        start, end  = 0, 0
        maxstart, maxend = 0, 0
        for idx in range(len(s)):
            #if char seen and last occurence lies within window
            if s[idx] in seen and start <= seen[s[idx]]:
                start = seen[s[idx]] + 1
            else:
                end = idx
                if end - start > maxend - maxstart:
                    maxend, maxstart = end, start
            #track last index of char
            seen[s[idx]] = idx



        return maxend - maxstart + 1 if len(s) > 0 else 0

assert 3 == lengthOfLongestSubstring("pwwkew")
assert 0 == lengthOfLongestSubstring("")
assert 1 == lengthOfLongestSubstring("bbbbb")
assert 3 == lengthOfLongestSubstring("abcabcbb")
