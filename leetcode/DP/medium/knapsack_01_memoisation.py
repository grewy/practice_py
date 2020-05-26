

def knapsack(wt, val, W, n):

    if n == 0 or W == 0:
        return 0

    if t[W][n] != -1:
        return t[W][n]

    if wt[-1] <= W:
        t[W][n] = max(val[-1] + knapsack(wt[:-1], val[:-1], W - wt[-1], n-1), knapsack(wt[:-1], val[:-1], W, n-1))
        return t[W][n]
    else:
        t[W][n] = knapsack(wt[:-1],   val[:-1], W, n-1)
        return t[W][n]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

t = [[-1]*(n+1)]*(W+1)

print knapsack(wt, val, W, n)
