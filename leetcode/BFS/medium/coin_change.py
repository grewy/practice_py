class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        visited = [False]*(amount+1)
        val = [0]
        visited[0] = True
        nc = 0

        while val:
            nval = []
            nc += 1
            while val:
                _val = val.pop(0)
                for coin in coins:
                    new_val = _val + coin
                    if new_val == amount:
                        return nc
                    elif  new_val < amount and not visited[new_val]:
                        visited[new_val] = True
                        nval.append(new_val)
            val = nval
        return -1


