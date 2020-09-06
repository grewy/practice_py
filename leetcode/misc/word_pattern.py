class Solution(object):
    def wordPattern(self, pattern, str1):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}
        str1 = str1.split()

        if len(pattern) != len(str1):
            return False

        for i in range(len(str1)):
            ch = 'char_' + pattern[i]
            word = 'word_' + str1[i]

            if d.get(ch) is None:
                d[ch] = i
            if d.get(word)is None:
                d[word] = i

            if d[ch] != d[word]:
                return False

        return True
