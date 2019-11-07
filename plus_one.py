def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ln = len(digits)
        idx = -1
        digits[idx] += 1
        carry = digits[idx] / 10
        digits[idx] %= 10
        idx -= 1
        while carry > 0 and abs(idx) <= ln:
            digits[idx] += carry
            carry = digits[idx] / 10
            digits[idx] %= 10
            idx -= 1

        if abs(idx) >= ln and carry > 0:
            digits.append(carry)
            nm = digits[-1]
            digits[1:] = digits[0:-1]
            digits[0] = nm

        return digits
