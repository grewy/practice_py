"""
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) == 0:
            return ['']

        res = []
        sub_res = self.letterCasePermutation(S[:-1])
        for sub in sub_res:
            if S[-1].isalpha():
                res.append(sub + S[-1].lower())
                res.append(sub + S[-1].upper())
            else:
                res.append(sub + S[-1])
        return res

S="a1b2"
print Solution().letterCasePermutation(S)
"""
"""

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        digits = {str(x) for x in range(10)}
        A = ['']
        for c in S:
            B = []
            if c in digits:
                for a in A:
                    B.append(a+c)
            else:
                for a in A:
                    B.append(a+c.lower())
                    B.append(a+c.upper())
            A=B

        return A

