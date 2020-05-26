

def knapsack(wt, val, W, n):

    if n == 0 or W == 0:
        return 0

    if wt[-1] <= W:
        return max(val[-1] + knapsack(wt[:-1], val[:-1], W - wt[-1], n-1), knapsack(wt[:-1], val[:-1], W, n-1))
    else:
        return knapsack(wt[:-1],   val[:-1], W, n-1)


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print knapsack(wt, val, W, n)
