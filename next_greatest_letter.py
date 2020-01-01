def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, r = 0, len(letters) - 1

        while l <= r:
            mid = (l+r)/2
            mid_val = ord(letters[mid])
            if mid_val > ord(target) and mid > 0 and ord(target) >= ord(letters[mid-1]):
                return letters[mid]
            elif mid_val > ord(target):
                r -= 1
            elif mid_val <= ord(target):
                l += 1

        return letters[0]
