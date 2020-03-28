class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, r = 0, len(letters) - 1
        tgt = ord(target)

        while l <= r:
            mid = (l+r)/2
            mid_val = ord(letters[mid])

            if mid_val > tgt and mid > 0 and tgt >= ord(letters[mid-1]):
                return letters[mid]

            elif mid_val > tgt:
                r -= 1

            elif mid_val <= tgt:
                l += 1

        return letters[0]
