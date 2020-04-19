class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        exp_dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in exp_dict.values():
                stack.append(char)
            elif char in exp_dict.keys():
                if stack == [] or exp_dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
