class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return '0'

        num = 0
        res = 0
        op = '+'
        s += '+'
        stack = []

        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == " ":
                pass
            else:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop()*num)
                elif op == "/":
                    operant = stack.pop()
                    sign = -1 if operant < 0 else 1
                    operant *= sign
                    stack.append(sign*(operant/num))

                num = 0
                op = ch

        return sum(stack)

