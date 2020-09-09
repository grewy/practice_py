class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        d = {3: "Fizz", 5: "Buzz"}

        for num in range(1, n+1):
            ans_str = ""
            for key in d.keys():
                if num % key == 0:
                    ans_str += d[key]
            if not ans_str:
                ans_str = str(num)
            ans.append(ans_str)

        return ans
