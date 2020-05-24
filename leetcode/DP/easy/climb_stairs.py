def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        memo = (1,2)
        for _ in range(2, n):
            memo = (memo[-1], memo[-1] + memo[-2])
        return memo[-1]

print climbStairs(3)
