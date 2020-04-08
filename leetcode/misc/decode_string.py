class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        stack = []

        for i in s:
            if (i.isalpha() or i.isdigit()) or i == '[':
                stack.append(i)
            elif i == ']':
                temp = ''
                while stack[-1] != '[':
                    temp = stack.pop()+ temp

                stack.pop() # pops '['
                times = ''
                while stack and stack[-1].isdigit():
                    times = stack.pop()+ times
                stack.append(temp*int(times))

        return ''.join(stack)
